from unittest import TestCase

from cplib.grid import build_rot90


class Test(TestCase):
    def test_rot_90(self) -> None:
        src = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        assert build_rot90(src) == [[6, 3, 0], [7, 4, 1], [8, 5, 2]]
        src = [[0, 1, 2], [3, 4, 5]]
        assert build_rot90(src) == [[3, 0], [4, 1], [5, 2]]
