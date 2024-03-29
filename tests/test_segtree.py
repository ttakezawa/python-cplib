from unittest import TestCase

from cplib.segtree import Segtree


class Test(TestCase):
    def test_segtree(self) -> None:
        seg_sum = Segtree([2.0, 4.0, 8.0], lambda a, b: a + b, 0.0)
        assert seg_sum.prod_range(0, 2) == 6.0
        seg_sum.add(0, 3.0)
        assert seg_sum.all_prod() == 17.0

        seg_max = Segtree([3, 5, 2], lambda a, b: max(a, b), 0)
        assert seg_max.prod_range(0, 2) == 5
