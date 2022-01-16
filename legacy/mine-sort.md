---
title: "Minesort, a cryptography based sort algorithm"
date: "2019-06-29T00:00:00Z"
draft: false
tags: ["algorithm", "sort", "joke", "cryptography"]
---

Mine sort is a cryptography based sorting algorithm that can run in $O(n)$ time
if you are lucky. It consists in two stages, the first one is to create a
cryptographic seed, and the second one is to check if the seed sorts the array.

Digging further into the first stage, this seed consists of the double hash of a
static content which previously is concatenated with a `seed` . This `seed` can
be anything, a random or sequential number or some string. The main goal of the
algorithm is to find the correct `seed` value which will sort the input. This is
better expressed via code, so here it is:

```python
key=sha256(str(sha256("Mine sort is the best "+str(seed))))
```

The second step is to try to sort the input based on the generated `key`. Given
that the generated hash can be expressed as a number, the algorithm generate
pairs of elements that will be swapped by applying the *mod* operator to the
content, and then dividing it by the size of the input, so the same value won't
be repeated. The following code express what was said on this paragraph:

```python
index1 = key % len(input)
key = key // len(input)
index2 = key % len(input)
key = key // len(input)
input[index1], input[index2] = input[index2], input[index1]
```

If this `seed` sorts the array, that is it ! You got your solution !
Congratulations, now you can apply your solution and sort your input in $o(n)$
time ! But for sure some quick sort fanatics will be butt hurt about this code
and will complain about the cryptography part of the code, this is just people
that don't accept an algorithm that can sort an input in a $o(n)$ !

## Complete source code

```python
#!/usr/bin/env python3
import hashlib

def sha256(data):
    digest = hashlib.new("sha256")
    digest.update(data)
    return int(digest.hexdigest(), 16)


def sort(input, key):
    input = input[:]
    val = key
    for i in range(0, len(input) -1):
        index1 = key % len(input)
        key = key // len(input)
        index2 = key % len(input)
        key = key // len(input)
        if key == 0:
            key = val
        input[index1], input[index2] = input[index2], input[index1]

    return all(input[i] <= input[i + 1] for i in range(len(input)-1))


def minesort(input):
    for seed in xrange(1,200000):
        key=sha256(str(sha256("Mine sort is the best "+str(seed))))
        if sort(input, key):
            return seed

    return None


print("Seed "+str(minesort([1,4,2,3,5,7,8,12,2])))
```
