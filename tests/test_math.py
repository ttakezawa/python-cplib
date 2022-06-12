from unittest import TestCase

from cplib.math import gcd, lcm


class Test(TestCase):
    def test_gcd(self) -> None:
        assert gcd(12, 8) == 4
        assert gcd(12, 6) == 6
        assert gcd(0, 42) == 42

    def test_lcm(self) -> None:
        assert lcm(8, 10) == 40
        assert lcm(3, 5) == 15
        assert lcm(0, 42) == 0
