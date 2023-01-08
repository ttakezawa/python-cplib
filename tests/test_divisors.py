from unittest import TestCase

from cplib.divisors import _divisors_with_trial_division, divisors


class Test(TestCase):
    def test_divisors(self) -> None:
        assert divisors(1) == [1]
        assert divisors(20) == [1, 2, 4, 5, 10, 20]
        assert len(divisors(9316358251200)) == 10752
        for i in range(1, 100):
            assert divisors(i) == _divisors_with_trial_division(i)
