from unittest import TestCase

from cplib.math_backport import comb, gcd, lcm, perm


class Test(TestCase):
    def test_gcd(self) -> None:
        assert gcd(12, 8) == 4
        assert gcd(12, 6) == 6
        assert gcd(0, 42) == 42
        assert gcd(1, 0) == 1
        assert gcd() == 0
        assert gcd(3) == 3
        assert gcd(24, 16, 4) == 4

    def test_lcm(self) -> None:
        assert lcm(8, 10) == 40
        assert lcm(3, 5) == 15
        assert lcm(0, 42) == 0
        assert lcm(1, 0) == 0
        assert lcm() == 1
        assert lcm(3) == 3
        assert lcm(6, 8, 12) == 24

    def test_comb(self) -> None:
        assert comb(100, 2) == 4950
        assert comb(35, 11) == 417225900
        assert comb(14, 4) == 1001
        assert comb(2, 0) == 1
        assert comb(0, 0) == 1
        assert comb(2, 3) == 0
        with self.assertRaises(ValueError):
            comb(2, -1)
        with self.assertRaises(ValueError):
            comb(-1, 3)

    def test_perm(self) -> None:
        assert perm(10, 3) == 720
        assert perm(0, 0) == 1
        assert perm(0, 1) == 0
        assert perm(2, 3) == 0
        with self.assertRaises(ValueError):
            perm(2, -1)
        with self.assertRaises(ValueError):
            perm(-1, 3)
