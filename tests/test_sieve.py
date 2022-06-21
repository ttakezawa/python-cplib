from unittest import TestCase

from cplib.sieve import Sieve


class Test(TestCase):
    def test_sieve(self) -> None:
        sieve = Sieve(20)
        assert sieve.get_primes() == [2, 3, 5, 7, 11, 13, 17, 19]
        assert sieve.factorize(1) == dict()
        assert sieve.factorize(2) == {2: 1}
        assert sieve.factorize(20) == {2: 2, 5: 1}
        assert sieve.divisors(1) == [1]
        assert sieve.divisors(20) == [1, 2, 4, 5, 10, 20]
