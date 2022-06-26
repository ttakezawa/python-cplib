from importlib.machinery import FrozenImporter
from typing import List

POW_MAX = 30


class LCAGraph:
    __slots__ = ("adj", "root", "parents", "depths")

    def __init__(self, adj: List[List[int]], root: int = 0) -> None:
        self.adj = adj
        self.root = root
        self.depths = [0] * len(adj)
        # parents[k][v] = 2^k nth parent of v
        self.parents = [[-1] * len(adj) for _ in range(POW_MAX + 1)]

        # prepare depths[v] and parents[0][v]
        self.depths[root] = 0
        st = [root]
        while st:
            v = st.pop()
            for u in adj[v]:
                if u == self.parents[0][v]:
                    continue
                self.parents[0][u] = v
                self.depths[u] = self.depths[v] + 1
                st.append(u)

        # prepare parents[k][v]
        for k in range(POW_MAX):
            for v in range(len(adj)):
                self.parents[k + 1][v] = self.parents[k][self.parents[k][v]]

    def lca(self, v: int, u: int) -> int:
        if self.depths[v] < self.depths[u]:
            v, u = u, v
        df = self.depths[v] - self.depths[u]
        for i in range(POW_MAX + 1):
            if df >> i & 1 == 1:
                v = self.parents[i][v]
        if v == u:
            return v
        for i in range(POW_MAX, -1, -1):
            if self.parents[i][v] != self.parents[i][u]:
                v, u = self.parents[i][v], self.parents[i][u]
        return self.parents[0][v]
