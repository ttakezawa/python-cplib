from functools import reduce
import math


def gcd(*integers: int) -> int:
    """O(log min(a,b))"""
    return reduce(math.gcd, integers, 0)


def lcm(*integers: int) -> int:
    """O(log min(a,b))"""
    return reduce(_lcm, integers, 1)


def _lcm(a: int, b: int) -> int:
    return a // math.gcd(a, b) * b
