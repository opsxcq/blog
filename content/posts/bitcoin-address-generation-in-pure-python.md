+++
title = "Bitcoin address generation in pure python"
author = ["OPSXCQ"]
date = 2018-09-14
draft = false
+++

This post is dedicated to explore the generation of `Bitcoin` key pairs using pure
python with no external libraries.

<!--more-->

The key pair generation can be archived in 4 steps:

-   Generating a secure private key.
-   Calculate the public key from the private key.
-   Encode the public key as a bitcoin address.
-   Encode the private key in the WIF format.


## Step 1: Generate ECDSA key pair {#step-1-generate-ecdsa-key-pair}

The very first step is to select a good and secure number, for this example we
won't use one, instead we will simply get the random from the system. An example
why is important a good and secure random number is [written in this post about
cracking some bitcoin private keys](https://strm.sh/post/bitcoin-transaction-nonce-reuse/), the bug isn't located in the key generation,
but in the random used to sign the transactions, but the point is the same, weak
PRNG (Pseudo-random number generators) can put everything in risk.

Using this PRNG can be done with:

```python
randomBytes = os.urandom(32)
```


## Step 2: Calculate the public key {#step-2-calculate-the-public-key}

Since bitcoin uses `spec256k` the only thing that we need to do is multiply it by
the initial point in the curve by the `private key` to obtain the public key.

Next step is to convert the key to a byte array and hash it, first with `SHA-256`
then with `RIPEMD-160`. Then we prepend the hashed public key with `0x00` if the
target network is the **mainnet**, if the address generated meant to be used in the
**testnet** `0x6f` must be prepended.

```python
SPEC256k1 = Point()
pk = int.from_bytes(privkey, "big")
hash160 = ripemd160(sha256((SPEC256k1 * pk).toBytes()))
address = b"\x00" + hash160
```


### Checksum {#checksum}

Then the only thing left to add in the address it the checksum, it is appended
to the address and is the last 4 bytes of the double `SHA-256` of the address
calculated above.

```python
address = b58(address + sha256(sha256(address))[:4])
```

Then just encode the key bytes to `base58` and you have your Bitcoin address !


## Step 3: Public key compression {#step-3-public-key-compression}

When representing the public key as a number is possible to compress it
considering that the key is \\(x\\) and \\(y\\) in the eliptic curve and since we have
the equation, and given an \\(x\\) value, there is only two values for \\(y\\) possible.
So to compress a public key, if \\(y\\) is odd, `0x03` is appended to the \\(x\\) value,
else, `0x02` is appended.


## Step 4: Encode the private key in the WIF format {#step-4-encode-the-private-key-in-the-wif-format}

To create a `WIF` key representation from the private key bytes is far simple than
the previous steps, first prepend the byte `0x80` to the `WIF`, then append the
private key bytes. After, append the checksum, that is the last 4 bytes of the
double `SHA-256` of the partial wif key that we already have calculated.

```python
wif = b"\x80" + privkey
wif = b58(wif + sha256(sha256(wif))[:4])
return wif
```


## Source code {#source-code}

This is a reference script, it depends on `Python 3` to run and is self contained,
it means no external dependencies are required to run it. One example of its
output:

```bash
$ ./bitcoin-address-generator.py
```

```text
Address: 18jJh1kSPJqbXtMB51SyczgcHL1drkDgxV
Privkey: 5JTEF3GHpDAin1caVqfznHU8T1jscHVVD5SMFALBTC4no2J4DqX
```


### Full Source code {#full-source-code}

```python
import os
import hashlib


def sha256(data):
    digest = hashlib.new("sha256")
    digest.update(data)
    return digest.digest()


def ripemd160(x):
    d = hashlib.new("ripemd160")
    d.update(x)
    return d.digest()


def b58(data):
    B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    if data[0] == 0:
        return "1" + b58(data[1:])

    x = sum([v * (256 ** i) for i, v in enumerate(data[::-1])])
    ret = ""
    while x > 0:
        ret = B58[x % 58] + ret
        x = x // 58

    return ret


class Point:
    def __init__(self,
        x=0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
        y=0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
        p=2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1):
        self.x = x
        self.y = y
        self.p = p

    def __add__(self, other):
        return self.__radd__(other)

    def __mul__(self, other):
        return self.__rmul__(other)

    def __rmul__(self, other):
        n = self
        q = None

        for i in range(256):
            if other & (1 << i):
                q = q + n
            n = n + n

        return q

    def __radd__(self, other):
        if other is None:
            return self
        x1 = other.x
        y1 = other.y
        x2 = self.x
        y2 = self.y
        p = self.p

        if self == other:
            l = pow(2 * y2 % p, p-2, p) * (3 * x2 * x2) % p
        else:
            l = pow(x1 - x2, p-2, p) * (y1 - y2) % p

        newX = (l ** 2 - x2 - x1) % p
        newY = (l * x2 - l * newX - y2) % p

        return Point(newX, newY)

    def toBytes(self):
        x = self.x.to_bytes(32, "big")
        y = self.y.to_bytes(32, "big")
        return b"\x04" + x + y


def getPublicKey(privkey):
    SPEC256k1 = Point()
    pk = int.from_bytes(privkey, "big")
    hash160 = ripemd160(sha256((SPEC256k1 * pk).toBytes()))
    address = b"\x00" + hash160

    address = b58(address + sha256(sha256(address))[:4])
    return address


def getWif(privkey):
    wif = b"\x80" + privkey
    wif = b58(wif + sha256(sha256(wif))[:4])
    return wif


if __name__ == "__main__":
    randomBytes = os.urandom(32)
    print("Address: " + getPublicKey(randomBytes))
    print("Privkey: " + getWif(randomBytes))
```


## References {#references}

-   [Eliptic curves in cryptography](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography)
-   [Bitcoin Address documentation](https://en.bitcoin.it/wiki/Address)
