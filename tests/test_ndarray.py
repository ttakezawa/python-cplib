from unittest import TestCase

from cplib.ndarray import ndarray


class Test(TestCase):
    def test_ndarray(self) -> None:
        assert ndarray([0], 1) == []
        assert ndarray([1], 2) == [2]
        assert ndarray((2, 3), 3) == [[3, 3, 3], [3, 3, 3]]
        assert ndarray([2, 3, 1], 4) == [[[4], [4], [4]], [[4], [4], [4]]]
