# Originated from
# - https://drken1215.hatenablog.com/entry/2020/10/31/203300
# - https://atcoder.jp/contests/abc177/editorial/82
from collections import defaultdict
from typing import Dict, List


class Sieve:
    __slots__ = (
        "_min_factor",
        "_primes",
    )

    def __init__(self, max: int) -> None:
        """O(n log log n)"""
        self._min_factor = [i for i in range(0, max + 1)]
        self._primes: List[int] = []
        for i in range(2, max + 1):
            if self._min_factor[i] != i:
                continue
            self._primes.append(i)
            for j in range(i * i, max + 1, i):
                if self._min_factor[j] == j:
                    self._min_factor[j] = i

    def get_primes(self) -> List[int]:
        return self._primes

    def is_prime(self, n: int) -> bool:
        return n > 1 and self._min_factor[n] == n

    def factorize(self, n: int) -> Dict[int, int]:
        """SPFによる素因数分解 O(log n): returns Dict[prime => count]"""
        ret: Dict[int, int] = defaultdict(int)
        while n > 1:
            ret[self._min_factor[n]] += 1
            n //= self._min_factor[n]
        return ret

    def divisors(self, n: int) -> List[int]:
        """O(√n)"""
        ret = [1]
        for factor, cnt in self.factorize(n).items():
            for j in range(0, len(ret)):
                p = 1
                for _ in range(cnt):
                    p *= factor
                    ret.append(p * ret[j])
        ret.sort()
        return ret
