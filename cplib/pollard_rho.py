# Originated from
# - https://qiita.com/Kiri8128/items/eca965fe86ea5f4cbb98
# - https://zenn.dev/mizar/articles/791698ea860581
# Verify
# - https://algo-method.com/tasks/553
# - https://algo-method.com/tasks/513
from math import gcd
from typing import Callable, Dict, Optional


def is_prime(n: int):
    """Miller-Rabin: ≒ O(1)"""
    if n == 2:
        return True
    if n < 2 or (n & 1) == 0:
        return False
    n1 = n - 1
    d, s = n1, 0
    while (d & 1) == 0:
        d //= 2
        s += 1
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        t = pow(a, d, n)
        if t == 1 or t == n1:
            continue
        for _ in range(s - 1):
            t = pow(t, 2, n)
            if t == n1:
                break
        else:
            return False
    return True


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


def divisors(n: int, prime_factors: Optional[Dict[int, int]] = None):
    """≲ O(n⁽¹/³⁾)"""
    if prime_factors == None:
        prime_factors = prime_factorize(n)
    ret: list[int] = [1]
    for p in prime_factors:
        ret_prev = ret
        ret = []
        for i in range(prime_factors[p] + 1):
            for r in ret_prev:
                ret.append(r * (p**i))
    return sorted(ret)


def _find_factor_rho(n: int) -> int:
    m = 1 << n.bit_length() // 8
    for c in range(1, 99):
        f: Callable[[int], int] = lambda x: (x * x + c) % n
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
