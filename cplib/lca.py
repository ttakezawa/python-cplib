from typing import List, Optional


class LCAGraph:
    __slots__ = (
        "depths",
        "ancestors",
    )

    def __init__(self, adj: List[List[int]], root: int = 0) -> None:
        self.depths = [0] * len(adj)

        # prepare depths[v] and parents[v] with DFS
        self.depths[root] = 0
        st = [root]
        parents = [root] * len(adj)
        while st:
            v = st.pop()
            for u in adj[v]:
                if u == parents[v]:
                    continue
                parents[u] = v
                self.depths[u] = self.depths[v] + 1
                st.append(u)
        bit_length = max(self.depths).bit_length()

        # prepare parents[k][v] = 2^k nth parent of v with doubling
        self.ancestors = [parents]
        for _ in range(1, bit_length):
            self.ancestors.append([self.ancestors[-1][v] for v in self.ancestors[-1]])

    def lca(self, v: int, u: int) -> int:
        if self.depths[v] < self.depths[u]:
            v, u = u, v
        df = self.depths[v] - self.depths[u]
        v = self.find_parent(v, df)  # type: ignore
        if v == u:
            return v
        for i in range(self.depths[v].bit_length() - 1, -1, -1):
            if self.ancestors[i][v] != self.ancestors[i][u]:
                v, u = self.ancestors[i][v], self.ancestors[i][u]
        return self.ancestors[0][v]

    def find_parent(self, v: int, dist: int) -> Optional[int]:
        if self.depths[v] < dist:
            return None
        for i in range(dist.bit_length()):
            if dist >> i & 1 == 1:
                v = self.ancestors[i][v]
        return v
