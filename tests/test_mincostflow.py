from typing import List
from unittest import TestCase

from cplib.mincostflow import MinCostFlowGraph


class Test(TestCase):
    def test_mincostflow(self) -> None:
        # https://atcoder.jp/contests/practice2/tasks/practice2_e
        def solve(N: int, K: int, grid: List[List[int]]):
            max_ = 1 << 30
            s = N + N
            t = N + N + 1
            g = MinCostFlowGraph(t + 1)
            for x in range(N):
                g.add_edge(s, x, K, 0)
            for y in range(N):
                g.add_edge(N + y, t, K, 0)

            for x in range(N):
                for y in range(N):
                    g.add_edge(x, N + y, 1, max_ - grid[y][x])

            g.add_edge(s, t, N * K, max_)
            flow, cost = g.flow(s, t, N * K)
            return max_ * flow - cost

        assert solve(3, 1, [[5, 3, 2], [1, 4, 8], [7, 6, 9]]) == 19
        assert solve(3, 2, [[10, 10, 1], [10, 10, 1], [1, 1, 10]]) == 50
