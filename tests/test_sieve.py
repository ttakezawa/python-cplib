from unittest import TestCase

from cplib.sieve import Sieve


class Test(TestCase):
    def test_sieve(self) -> None:
        sieve = Sieve(20)
        assert sieve.get_primes() == [2, 3, 5, 7, 11, 13, 17, 19]
        assert sieve.factorize(20) == {2: 2, 5: 1}
        divs = sieve.divisors(20)
        divs.sort()
        assert divs == [1, 2, 4, 5, 10, 20]
