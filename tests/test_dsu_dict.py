from unittest import TestCase

from cplib.dsu_dict import DSUDict


class Test(TestCase):
    def test_dsu(self) -> None:
        dsu = DSUDict()
        dsu.merge(0, 8)
        dsu.merge(1, 2)
        dsu.merge(2, 3)
        assert dsu.same(0, 8) == True
        assert dsu.same(1, 3) == True
        assert dsu.same(5, 5) == True
        assert dsu.same(0, 5) == False
        assert dsu.groups() == {0: [0, 8], 1: [1, 2, 3], 5: [5]}
