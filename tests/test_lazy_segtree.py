from unittest import TestCase

from cplib.lazy_segtree import LazySegtree


class Test(TestCase):
    def test_segtree(self) -> None:
        seg = LazySegtree(
            [2] * 5,
            0,
            lambda a, b: max(a, b),
            1,
            lambda f, x: f * x,
            lambda f, g: f * g,
        )
        assert seg.all_prod() == 2
        seg.apply(0, 4, 2)
        assert seg.all_prod() == 4
