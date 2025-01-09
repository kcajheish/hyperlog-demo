from hashlib import sha256
from math import log, sqrt, pow

class HyperLog:
    def __init__(self, p):
        self.p = p
        self.m = int(pow(2, p))
        self.buckets = [0 for _ in range(self.m)]
        self.hash = sha256
        self.WORD_LEN = 32
        self.BYTE_TO_BIT = 8

    def count_leading_zero(self, num, k):
        count = 0
        for i in range(k-1, -1, -1):
            if (num & (1 << i)) > 0:
                break
            count += 1
        return count

    def insert(self, key):
        h = self.hash(key.encode())
        # byte string for 32 bit word
        byte_in_word = int(self.WORD_LEN/self.BYTE_TO_BIT)
        word = h.digest()[:byte_in_word]

        # turn byte string into word
        word_in_int = int.from_bytes(word)
        last_bit = self.WORD_LEN - self.p
        head = word_in_int >> last_bit
        self.buckets[head] = max(
            self.buckets[head],
            self.count_leading_zero(word_in_int - head, last_bit) + 1
        )

    def alpha(self):
        return 0.7213/(1+ 1.079/self.m)

    def cardinality(self):
        E =  self.alpha() * pow(self.m, 2) / sum([ pow(2, -n) for n in self.buckets])
        E_star = E
        N = 1 << 32
        if E <= 2.5 * self.m:
            v = self.buckets.count(0)
            if v > 0:
                E_star = self.m * log(self.m/v, 10)
        elif E > N / 30:
            E_star = -N*log(1-E/N)
        return E_star

    def error(self):
        return 1.04 / sqrt(self.m)
