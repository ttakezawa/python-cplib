from unittest import TestCase

from cplib.modular import FactorialCache, inv_mod, mod1000000007, pow_mod


class Test(TestCase):
    def test_pow_mod(self) -> None:
        def naive(x: int, n: int, mod: int) -> int:
            x %= mod
            r = 1 % mod
            for _ in range(n):
                r = r * x % mod
            return r

        for a in range(-100, 70):
            for b in range(0, 20):
                for c in range(1, 101):
                    assert naive(a, b, c) == pow_mod(a, b, c)

    def test_inv_mod(self) -> None:
        assert inv_mod(1, 13) == 1
        assert inv_mod(2, 13) == 7
        assert inv_mod(3, 13) == 9
        assert inv_mod(4, 13) == 10
        assert inv_mod(5, 13) == 8

    def test_combination(self) -> None:
        fc = FactorialCache(int(5e6), mod1000000007)
        assert fc.combination(2, 3) == 0
        assert fc.combination(2, 0) == 1
        assert fc.combination(5, 2) == 10
        assert fc.combination(7, 3) == 35
        assert fc.factorial(100) == 437918130
