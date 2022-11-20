from unittest import TestCase

from cplib.lazy_segtree import LazySegtree


class Test(TestCase):
    def test_lazy_segtree(self) -> None:
        seg = LazySegtree(
            [2] * 5,
            lambda a, b: max(a, b),
            0,
            lambda f, x: f * x,
            lambda f, g: f * g,
            1,
        )
        assert seg.all_prod() == 2
        seg.apply_range(0, 4, 2)
        assert seg.all_prod() == 4
