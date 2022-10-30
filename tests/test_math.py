from unittest import TestCase

from cplib.math import next_permutation


class Test(TestCase):
    def test_next_permutation(self) -> None:
        xs = [1, 2, 3]
        expects = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        for expect in expects[:-1]:
            assert xs == expect
            assert next_permutation(xs) == True
        assert xs == expects[-1]
        assert next_permutation(xs) == False
        assert xs == expects[-1]

        xs = ["a", "bb", "c"]
        assert next_permutation(xs) == True
        assert xs == ["a", "c", "bb"]
