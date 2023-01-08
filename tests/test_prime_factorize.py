from unittest import TestCase

from cplib.prime_factorize import _prime_factorize_with_trial_division, prime_factorize


class Test(TestCase):
    def test_prime_factorize(self) -> None:
        assert prime_factorize(1) == dict()
        assert prime_factorize(2) == {2: 1}
        assert prime_factorize(20) == {2: 2, 5: 1}
        assert prime_factorize(2023) == {7: 1, 17: 2}
        for i in range(1, 100):
            assert prime_factorize(i) == _prime_factorize_with_trial_division(i)
