from unittest import TestCase

from cplib.divisors import divisors


class Test(TestCase):
    def test_divisors(self) -> None:
        assert divisors(1) == [1]
        assert divisors(20) == [1, 2, 4, 5, 10, 20]
