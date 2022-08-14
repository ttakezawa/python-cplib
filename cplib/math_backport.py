from functools import reduce
import math
from operator import index
from typing import Optional

# Changed in version 3.9: Added support for an arbitrary number of arguments. Formerly, only two arguments were supported.
def gcd(*integers: int) -> int:
    """O(log min(a,b))"""
    return reduce(math.gcd, integers, 0)


# New in version 3.9.
def lcm(*integers: int) -> int:
    """O(log min(a,b))"""
    return reduce(_lcm, integers, 1)


def _lcm(a: int, b: int) -> int:
    return a // math.gcd(a, b) * b


# New in version 3.8.
# https://github.com/mozillazg/pypy/blob/release-pypy3.9-v7.3.9/pypy/module/math/app_math.py#L175
def comb(n: int, k: int, /) -> int:
    n = index(n)
    k = index(k)

    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if k < 0:
        raise ValueError("k must be a non-negative integer")
    if k > n:
        return 0
    k = min(k, n - k)
    num, den = 1, 1
    for i in range(k):
        num = num * (n - i)
        den = den * (i + 1)

    return num // den


# New in version 3.8.
# https://github.com/mozillazg/pypy/blob/release-pypy3.9-v7.3.9/pypy/module/math/app_math.py#L206
def perm(n: int, k: Optional[int] = None, /) -> int:
    n = index(n)
    if k is None:
        k = n
    else:
        k = index(k)

    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if k < 0:
        raise ValueError("k must be a non-negative integer")
    if k > n:
        return 0

    res = 1
    for x in range(n, n - k, -1):
        res *= x
    return res
