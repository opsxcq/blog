+++
title = "Bitcoin nonce reuse vulnerability"
date = 2018-08-09T00:00:00Z
draft = true
tags = ["cryptography", "bitcoin", "blockchain"]
+++

Analyse Bitcoin blockchain. Found **XX vulnerable transactions** **XX private
keys** were recovered summing up **XX btcs** which at this moment worth **XXX
dollars**.

![wallet](/img/bitcoin-nonce-reuse-wallet.png)


# Concept

When the nonce is reused it become vulnerable and result in a trivial equation
to be solved.

$$
Key = ((r \times (s_1 - s_2))^{p - 2} \mod{p}) \times ((m_1 \times s_2) - (m_2 \times s_1)) \mod{p}
$$

Where:

- $p$ Is a constant value defined by the $n$ value of [secp256k1](https://en.bitcoin.it/wiki/Secp256k1): $115792089237316195423570985008687907852837564279074904382605163141518161494337$
- $r$ and $s$ which are the [ECDSA signature pair](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm)
- $m$ is the message to be signed, in this scenario, is the value that [*OP_CHECKSIG* will verify](https://en.bitcoin.it/wiki/OP_CHECKSIG)

Translating this equation as *Java* code it looks like:


```java
String pValue = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141";
BigInteger p = new BigInteger(pValue, 16);
BigInteger privateKey = 
r.multiply(
           s1.subtract(s2)
          ).modPow(
                   p.subtract(BigInteger.valueOf(2)), p
                  ).
          multiply(
                   m1.multiply(s2).subtract(m2.multiply(s1))
                  ).mod(p);
```

A similar vulnerability found on
[PS3](https://events.ccc.de/congress/2010/Fahrplan/attachments/1780_27c3_console_hacking_2010.pdf).

The rest of the process is pretty straight forward, in a pseudo-code it is:

```python
for block in blocks:
  for transaction in block:
    attack(transaction)
```

# Vulnerable keys

- Summarize the amount of bitcoins that those addresses had
- List vulnerable keys found

