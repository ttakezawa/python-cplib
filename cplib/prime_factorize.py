# Originated from https://qiita.com/Kiri8128/items/eca965fe86ea5f4cbb98
# Verify https://algo-method.com/tasks/553
import typing
from collections import defaultdict as __defaultdict
from math import gcd

from .miller_rabin import is_prime


def prime_factorize(n: int):
    """O(n⁽¹/⁴⁾)"""
    i = 2
    ret: dict[int, int] = {}
    rhoFlg = 0
    while i * i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        if k:
            ret[i] = k
        i += i % 2 + (3 if i % 3 == 1 else 1)
        if i == 101 and n >= 2**20:
            while n > 1:
                if is_prime(n):
                    ret[n], n = 1, 1
                else:
                    rhoFlg = 1
                    j = _find_factor_rho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                    ret[j] = k
    if n > 1:
        ret[n] = 1
    if rhoFlg:
        ret = {x: ret[x] for x in sorted(ret)}
    return ret


def _find_factor_rho(n: int) -> int:
    m = 1 << n.bit_length() // 8
    for c in range(1, 99):
        f: typing.Callable[[int], int] = lambda x: (x * x + c) % n
        y, r, q, g = 2, 1, 1, 1
        x, ys = 0, 0
        while g == 1:
            x = y
            for _ in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = f(ys)
                g = gcd(abs(x - ys), n)
        if g < n:
            if is_prime(g):
                return g
            elif is_prime(n // g):
                return n // g
            return _find_factor_rho(g)
    return -1


def _prime_factorize_with_trial_division(n: int):
    """O(√n)"""
    ret: dict[int, int] = __defaultdict(int)
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
