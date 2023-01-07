from unittest import TestCase

from cplib.factorize import factorize


class Test(TestCase):
    def test_factorize(self) -> None:
        assert factorize(1) == dict()
        assert factorize(2) == {2: 1}
        assert factorize(20) == {2: 2, 5: 1}
        assert factorize(2023) == {7: 1, 17: 2}
