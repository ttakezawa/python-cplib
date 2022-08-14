from unittest import TestCase

from cplib.integer import gcd, lcm


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