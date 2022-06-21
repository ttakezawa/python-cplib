from typing import List


def divisors(n: int) -> List[int]:
    """O(√n)"""
    ret: List[int] = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
        i += 1
    ret.sort()
    return ret
