from unittest import TestCase

from cplib.miller_rabin import is_prime


class Test(TestCase):
    def test_is_prime(self) -> None:
        assert not is_prime(57)
        assert is_prime(10**9 + 7)
        assert is_prime(998244353)

        from cplib.sieve import Sieve

        sieve = Sieve(100)
        for i in range(1, 100):
            assert is_prime(i) == sieve.is_prime(i)
