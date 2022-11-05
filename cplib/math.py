from typing import Any, List, Tuple


def ext_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """solves ax + by = gcd(a, b) and returns gcd, x, y"""
    if a == 0:
        return b, 0, 1
    g, y, x = ext_gcd(b % a, a)
    return g, x - (b // a) * y, y


def next_permutation(a: List[Any]) -> bool:
    for i in range(len(a) - 2, -1, -1):
        if a[i] >= a[i + 1]:
            continue
        for j in range(len(a) - 1, i, -1):
            if a[i] >= a[j]:
                continue
            a[i], a[j], p, q = a[j], a[i], i + 1, len(a) - 1
            while p < q:
                a[p], a[q], p, q = a[q], a[p], p + 1, q - 1
            return True
    return False


def prev_permutation(a: List[Any]) -> bool:
    for i in range(len(a) - 2, -1, -1):
        if a[i] <= a[i + 1]:
            continue
        for j in range(len(a) - 1, i, -1):
            if a[i] <= a[j]:
                continue
            a[i], a[j], p, q = a[j], a[i], i + 1, len(a) - 1
            while p < q:
                a[p], a[q], p, q = a[q], a[p], p + 1, q - 1
            return True
    return False
