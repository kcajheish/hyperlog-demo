# Introduction
HyperLog calculates approximated cardinality in a multiset. It is practical when cardinality is high, and linear-space counting takes a lot of memory.

Imagine receiving a stream of random values. One of values has two leading zero, $<001>_2$. The probability of two zeros in a row is $0.5^3 = 0.125$. In other words, ${1\over 0.125} = 8$ values are needed so that one of them is a $<001>_2$. If there are k leading zeros in a binary, you might have seen $2^{k+1}$ in total.

Consider another case: $<100001>_2$ comes before $<001001>_2$. Their probability is the same due to same number of zeros, but their estimated count, 2 and 8, has a difference of 4 times. That is huge.

To reduce the variance, buckets are introduced. In the previous case, assume first three bits are reserved as the bucket number. Now, both values become $<001>_2$. The only difference is that first value belongs to the 4th bucket while second value belongs to the 1st. The estimated count for both values is now the same.

These are the ideas behind the HyperLog. The implementation details can be checked in the reference.

# Setup and Result
hash function: SHA-256

word length: 32 bit

bucket size: 12 bit

number of unique input: 100000

estimated cardinality: 100167.60

actual error: 0.17

expected error: 0.016

# Test
```code
python -m unittest discover
```

# Reference
https://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf
https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/40671.pdf
https://stackoverflow.com/questions/12327004/how-does-the-hyperloglog-algorithm-work
https://en.wikipedia.org/wiki/HyperLogLog

