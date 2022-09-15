from collections import defaultdict as __defaultdict
from typing import Dict as _Dict


def factorize(n: int) -> _Dict[int, int]:
    """O(√n)"""
    ret: _Dict[int, int] = __defaultdict(int)
    i = 2
    while i * i <= n:
        while n % i == 0:
            ret[i] += 1
            n //= i
        i += 1
    if n > 1:
        ret[n] = 1
    return ret
