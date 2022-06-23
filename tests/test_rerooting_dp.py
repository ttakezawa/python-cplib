from typing import List
from unittest import TestCase

from cplib.rerooting_dp import rerooting_dp


class Test(TestCase):
    def test_rerooting_dp(self) -> None:
        m = 2
        edges = [
            (8, 5),
            (10, 8),
            (6, 5),
            (1, 5),
            (4, 8),
            (2, 10),
            (3, 6),
            (9, 2),
            (1, 7),
        ]

        adj: List[List[int]] = [[] for _ in range(10)]
        for (u, v) in edges:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

        dp = rerooting_dp(
            adj,
            1,
            lambda x, y: x * y % m,
            lambda x, to, from_: x + 1,
            lambda x, v: x,
        )
        assert dp == [0, 0, 1, 1, 1, 0, 1, 0, 1, 1]
