from unittest import TestCase

from cplib.pollard_rho import divisors, prime_factorize


class Test(TestCase):
    def test_prime_factorize(self) -> None:
        assert prime_factorize(1) == dict()
        assert prime_factorize(2) == {2: 1}
        assert prime_factorize(20) == {2: 2, 5: 1}
        assert prime_factorize(2023) == {7: 1, 17: 2}

    def test_divisors(self) -> None:
        assert divisors(1) == [1]
        assert divisors(20) == [1, 2, 4, 5, 10, 20]
