from unittest import TestCase

from cplib.modular import ModFactorialCache, mod_inv, mod1000000007, mod_pow


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
                    assert naive(a, b, c) == mod_pow(a, b, c)

    def test_inv_mod(self) -> None:
        assert mod_inv(1, 13) == 1
        assert mod_inv(2, 13) == 7
        assert mod_inv(3, 13) == 9
        assert mod_inv(4, 13) == 10
        assert mod_inv(5, 13) == 8

    def test_comb(self) -> None:
        fc = ModFactorialCache(int(5e6), mod1000000007)
        assert fc.comb(100, 2) == 4950
        assert fc.comb(35, 11) == 417225900
        assert fc.comb(14, 4) == 1001
        assert fc.comb(0, 0) == 1
        assert fc.comb(2, 0) == 1
        assert fc.comb(2, 3) == 0
        assert fc.factorial(100) == 437918130
