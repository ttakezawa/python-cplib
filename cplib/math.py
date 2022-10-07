from typing import Tuple


def ext_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """solves ax + by = gcd(a, b) and returns gcd, x, y"""
    if a == 0:
        return b, 0, 1
    g, y, x = ext_gcd(b % a, a)
    return g, x - (b // a) * y, y
