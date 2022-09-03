from typing import List
from unittest import TestCase

from cplib.lca import LCAGraph


class Test(TestCase):
    def test_lca(self) -> None:
        adj: List[List[int]] = [[] for _ in range(100000)]
        edges = [(0, 1), (2, 0), (3, 1), (1, 4), (0, 99_999)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        g = LCAGraph(adj)
        assert 0 == g.lca(0, 0)
        assert 0 == g.lca(0, 1)
        assert 0 == g.lca(0, 2)
        assert 0 == g.lca(0, 3)
        assert 0 == g.lca(0, 4)
        assert 0 == g.lca(0, 99999)
        assert 0 == g.lca(1, 2)
        assert 1 == g.lca(1, 3)
        assert 1 == g.lca(1, 4)
        assert 0 == g.lca(2, 3)
        assert 0 == g.lca(2, 4)
        assert 1 == g.lca(3, 4)

    def test_find_parent(self) -> None:
        adj: List[List[int]] = [[] for _ in range(100000)]
        edges = [(0, 1), (2, 0), (3, 1), (1, 4), (0, 99_999)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        g = LCAGraph(adj)
        assert 0 == g.find_parent(0, 0)
        assert None == g.find_parent(0, 1)
        assert 0 == g.find_parent(1, 1)
        assert None == g.find_parent(1, 2)

    def test_dist(self) -> None:
        adj: List[List[int]] = [[] for _ in range(100000)]
        edges = [(0, 1), (2, 0), (3, 1), (1, 4), (0, 99_999)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        g = LCAGraph(adj)
        assert 0 == g.dist(2, 2)
        assert 1 == g.dist(0, 1)
        assert 3 == g.dist(2, 3)

    def test_goto(self) -> None:
        adj: List[List[int]] = [[] for _ in range(100000)]
        edges = [(0, 1), (2, 0), (3, 1), (1, 4), (0, 99_999)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        g = LCAGraph(adj)
        assert 0 == g.goto(0, 4, 0)
        assert 1 == g.goto(0, 4, 1)
        assert 4 == g.goto(0, 4, 2)
        assert None == g.goto(0, 4, 3)
        assert 0 == g.goto(2, 3, 1)
        assert 3 == g.goto(2, 3, 3)
        assert None == g.goto(2, 3, 4)
