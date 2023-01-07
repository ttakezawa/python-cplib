from collections import defaultdict as __defaultdict
from typing import Dict as _Dict


def prime_factorize(n: int) -> _Dict[int, int]:
    """O(√n)"""
    ret: _Dict[int, int] = __defaultdict(int)
    while n & 1 == 0:
        ret[2] += 1
        n >>= 1
    i = 3
    while i * i <= n:
        while n % i == 0:
            ret[i] += 1
            n //= i
        i += 2
    if n > 1:
        ret[n] = 1
    return ret
