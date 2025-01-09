# Introduction
HyperLog calculates approximated cardinality in a multiset. It is practical when cardinality is high, and linear space counting takes a lot of memory.

Imagine receiving a stream of random value. One of them has two leading zero, $<001>_2$. The probability of two zero in a row is $0.5^3 = 0.125$. In other word, ${1\over 0.125} = 8$ values are needed so that one of them is a $<001>_2$. If there are k leading zero in a binary, you might have seen $2^{k+1}$ in total.

Consider another case: $<100001>_2$ comes before $<001001>_2$. Their probability is the same due to same number of zero, but their estimated count, 2 and 8, has 4 times difference. That is huge.

To reduce the variance, bucket is introduced. In previous case, assume first three bits are reserved as bucket number. Now, both values become $<001>_2$. The only difference is that first value belongs to 4th bucket while second value belongs to 1th. The estimated count for both value is now the same.

These are the ideas behind the hyperlog. The implementation details can be checked in reference.

# Setup and Result
hash function: SHA-256

word length: 32 bit

bucket size: 12 bit

number of unique input: 100000

estimated cardinality: 100167.60

actual error: 0.17

expect error: 0.016

# Test
```code
python -m unittest discover
```

# Reference
https://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf
https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/40671.pdf
https://stackoverflow.com/questions/12327004/how-does-the-hyperloglog-algorithm-work
https://en.wikipedia.org/wiki/HyperLogLog

