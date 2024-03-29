import math
from functools import reduce as _reduce
from operator import index
from typing import Iterable, Optional


# Changed in version 3.9: Added support for an arbitrary number of arguments. Formerly, only two arguments were supported.
def gcd(*integers: int) -> int:
    """O(log min(a,b))"""
    return _reduce(math.gcd, integers, 0)


# New in version 3.9.
def lcm(*integers: int) -> int:
    """O(log min(a,b))"""
    return _reduce(_lcm, integers, 1)


def _lcm(a: int, b: int) -> int:
    return a // math.gcd(a, b) * b


# New in version 3.8.
# https://github.com/mozillazg/pypy/blob/release-pypy3.9-v7.3.9/pypy/module/math/app_math.py#L175
def comb(n: int, k: int) -> int:
    """Number of ways to choose k items from n items without repetition and without order."""
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
def perm(n: int, k: Optional[int] = None) -> int:
    """Number of ways to choose k items from n items without repetition and with order."""
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


# New in version 3.8.
# https://github.com/mozillazg/pypy/blob/release-pypy3.9-v7.3.9/pypy/module/math/interp_math.py#L153
def dist(p: Iterable[float], q: Iterable[float]) -> float:
    """Return the Euclidean distance between two points p and q."""
    p = list(p)
    q = list(q)
    if len(p) != len(q):
        raise ValueError("both points must have the same number of dimensions")
    return math.sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))


# New in version 3.10.
def bit_count(x: int):
    """Return the number of ones in the binary representation of the absolute value of the integer. This is also known as the population count."""
    x -= (x >> 1) & 0x5555555555555555
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0F0F0F0F0F0F0F0F
    x += x >> 8
    x += x >> 16
    x += x >> 32
    return x & 0x7F
