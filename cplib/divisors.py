# Verify https://algo-method.com/tasks/344
import typing

from .prime_factorize import prime_factorize


def divisors(n: int, prime_factors: typing.Optional[typing.Dict[int, int]] = None):
    """≲ O(n⁽¹/³⁾)"""
    if prime_factors == None:
        prime_factors = prime_factorize(n)
    ret: list[int] = [1]
    for p in prime_factors:
        ret, ret_prev = [], ret
        for i in range(prime_factors[p] + 1):
            for r in ret_prev:
                ret.append(r * (p**i))
    return sorted(ret)


def _divisors_with_trial_division(n: int):
    """O(√n)"""
    ret: list[int] = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
        i += 1
    ret.sort()
    return ret
