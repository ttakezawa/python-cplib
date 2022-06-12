from unittest import TestCase
from cplib.math import gcd

class Test(TestCase):
    def test_gcd(self):
        assert gcd(12,8) == 4
        assert gcd(12,6) == 6
        assert gcd(0,42) == 42
