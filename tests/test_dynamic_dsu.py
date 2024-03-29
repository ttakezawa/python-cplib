from unittest import TestCase

from cplib.dynamic_dsu import DynamicDSU


class Test(TestCase):
    def test_dsu(self) -> None:
        dsu: DynamicDSU[int] = DynamicDSU()
        dsu.merge(0, 8)
        dsu.merge(1, 2)
        dsu.merge(2, 3)
        assert dsu.same(0, 8) == True
        assert dsu.same(1, 3) == True
        assert dsu.same(5, 5) == True
        assert dsu.same(0, 5) == False
        assert sorted(dsu.groups()) == sorted([[0, 8], [1, 2, 3], [5]])

        assert dsu.size(0) == 2
        assert dsu.size(1) == 3
        assert dsu.size(2) == 3
        assert dsu.size(3) == 3
        assert dsu.size(8) == 2

        assert dsu.leader(1001) == 1001
        assert dsu.size(1002) == 1
