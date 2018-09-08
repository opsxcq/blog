+++
title = "Bitcoin nonce reuse vulnerability"
date = 2018-08-09T00:00:00Z
draft = true
tags = ["cryptography", "bitcoin", "blockchain"]
+++

Analyse Bitcoin blockchain. Found **XX vulnerable transactions** summing up **XX
btcs** which at this moment worth **XXX dollars**.

![wallet](/img/bitcoin-nonce-reuse-wallet.png)


# Concept

- When the nonce is reused it become vulnerable


<style>
#MathJax-Span-3 > span:nth-child(1){
max-width: unset;
}
</style>

$$
Key = ((r \times (s_1 - s_2))^{p - 2} \mod{p}) \times ((m_1 \times s_2) - (m_2 \times s_1)) \mod{p}
$$

Where $p=115792089237316195423570985008687907852837564279074904382605163141518161494337$

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

# Vulnerable keys

- Summarize the amount of bitcoins that those addresses had
- List vulnerable keys found

