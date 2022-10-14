from unittest import TestCase

from cplib.maxflow import MaxflowGraph


class Test(TestCase):
    def test_flow(self) -> None:
        g = MaxflowGraph(6)
        edges = [
            (1, 2, 5),
            (1, 4, 4),
            (2, 3, 4),
            (2, 5, 7),
            (3, 6, 3),
            (4, 5, 3),
            (5, 6, 5),
        ]
        for s, t, cap in edges:
            g.add_edge(s - 1, t - 1, cap)

        assert g.flow(0, 5) == 8
