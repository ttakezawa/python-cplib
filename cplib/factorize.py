from collections import defaultdict
from typing import Dict


def factorize(n: int) -> Dict[int, int]:
    """O(√n)"""
    ret: Dict[int, int] = defaultdict(int)
    i = 2
    while i * i <= n:
        while n % i == 0:
            ret[i] += 1
            n //= i
        i += 1
    if n > 1:
        ret[n] = 1
    return ret
