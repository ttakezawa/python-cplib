from unittest import TestCase

from cplib.potential_dsu import PotentialDSU


class Test(TestCase):
    def test_dsu(self) -> None:
        dsu = PotentialDSU(6)
        dsu.merge(0, 4, 1)
        dsu.merge(1, 2, 1)
        dsu.merge(2, 3, 1)
        assert dsu.same(0, 4) == True
        assert dsu.same(1, 3) == True
        assert dsu.same(5, 5) == True
        assert dsu.same(0, 5) == False
        assert dsu.groups() == [[0, 4], [1, 2, 3], [5]]

        assert dsu.size(0) == 2
        assert dsu.size(1) == 3
        assert dsu.size(2) == 3
        assert dsu.size(3) == 3
        assert dsu.size(4) == 2

        assert dsu.diff(0, 4) == 1
        assert dsu.diff(1, 3) == 2
