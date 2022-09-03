from distutils.command.build import build
from typing import List
from unittest import TestCase

from cplib.graph import diameter, build_dist


class Test(TestCase):
    def test_diameter(self) -> None:
        adj: List[List[int]] = [[] for _ in range(100000)]
        edges = [(0, 1), (2, 0), (3, 1), (1, 4), (0, 99_999)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        assert (3, 2, [3, 1, 0, 2]) == diameter(adj)

    def test_build_dist(self) -> None:
        adj: List[List[int]] = [[] for _ in range(6)]
        edges = [(0, 1), (2, 0), (3, 1), (1, 4), (0, 5)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        assert [0, 1, 1, 2, 2, 1] == build_dist(adj, 0)
