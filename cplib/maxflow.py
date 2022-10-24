# SEE: https://atcoder.github.io/ac-library/production/document_ja/maxflow.html
# Originated from https://github.com/not522/ac-library-python/blob/master/atcoder/maxflow.py
from typing import List, NamedTuple, Optional, cast


class MaxFlowGraph:
    class Edge(NamedTuple):
        src: int
        dst: int
        cap: int
        flow: int

    class _Edge:
        def __init__(self, dst: int, cap: int) -> None:
            self.dst, self.cap = dst, cap
            self.rev: Optional[MaxFlowGraph._Edge] = None

    def __init__(self, n: int) -> None:
        self._n = n
        self._g: List[List[MaxFlowGraph._Edge]] = [[] for _ in range(n)]
        self._edges: List[MaxFlowGraph._Edge] = []

    def add_edge(self, src: int, dst: int, cap: int) -> int:
        assert 0 <= src < self._n
        assert 0 <= dst < self._n
        assert 0 <= cap
        m = len(self._edges)
        e, re = MaxFlowGraph._Edge(dst, cap), MaxFlowGraph._Edge(src, 0)
        e.rev, re.rev = re, e
        self._g[src].append(e)
        self._g[dst].append(re)
        self._edges.append(e)
        return m

    def get_edge(self, i: int) -> Edge:
        assert 0 <= i < len(self._edges)
        e = self._edges[i]
        re = cast(MaxFlowGraph._Edge, e.rev)
        return MaxFlowGraph.Edge(re.dst, e.dst, e.cap + re.cap, re.cap)

    def edges(self) -> List[Edge]:
        return [self.get_edge(i) for i in range(len(self._edges))]

    def change_edge(self, i: int, new_cap: int, new_flow: int) -> None:
        assert 0 <= i < len(self._edges)
        assert 0 <= new_flow <= new_cap
        e = self._edges[i]
        e.cap = new_cap - new_flow
        assert e.rev is not None
        e.rev.cap = new_flow

    def flow(self, s: int, t: int, flow_limit: Optional[int] = None) -> int:
        """
        O(min(n^(2/3) m,m^(3/2))) (if all the capacities are 1) or
        O(n^2 m) (general)
        """
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t
        if flow_limit is None:
            flow_limit = sum(e.cap for e in self._g[s])

        current_edge, level = [0] * self._n, [0] * self._n

        def fill(arr: List[int], value: int) -> None:
            for i in range(len(arr)):
                arr[i] = value

        def bfs() -> bool:
            fill(level, self._n)
            queue = [s]
            q_front, level[s] = 0, 0
            while q_front < len(queue):
                v = queue[q_front]
                q_front += 1
                next_level = level[v] + 1
                for e in self._g[v]:
                    if e.cap == 0 or level[e.dst] <= next_level:
                        continue
                    level[e.dst] = next_level
                    if e.dst == t:
                        return True
                    queue.append(e.dst)
            return False

        def dfs(lim: int) -> int:
            stack = [t]
            edge_stack: List[MaxFlowGraph._Edge] = []
            while stack:
                v = stack[-1]
                if v == s:
                    flow = min(lim, min(e.cap for e in edge_stack))
                    for e in edge_stack:
                        e.cap -= flow
                        assert e.rev is not None
                        e.rev.cap += flow
                    return flow
                next_level = level[v] - 1
                while current_edge[v] < len(self._g[v]):
                    e = self._g[v][current_edge[v]]
                    re = cast(MaxFlowGraph._Edge, e.rev)
                    if level[e.dst] != next_level or re.cap == 0:
                        current_edge[v] += 1
                        continue
                    stack.append(e.dst)
                    edge_stack.append(re)
                    break
                else:
                    stack.pop()
                    if edge_stack:
                        edge_stack.pop()
                    level[v] = self._n
            return 0

        flow = 0
        while flow < flow_limit:
            if not bfs():
                break
            fill(current_edge, 0)
            while flow < flow_limit:
                f = dfs(flow_limit - flow)
                flow += f
                if f == 0:
                    break
        return flow

    def min_cut(self, s: int) -> List[bool]:
        """O(n+m): 長さnのlistを返す。i番目の要素には、頂点sからiへ残余グラフで到達可能なときtrueを返す。flow(s,t)をflow_limitなしでちょうど一回呼んだ後に呼ぶと、返り値はs,t間のmincutに対応します。"""
        visited = [False] * self._n
        visited[s] = True
        stack = [s]
        while stack:
            v = stack.pop()
            for e in self._g[v]:
                if e.cap > 0 and not visited[e.dst]:
                    visited[e.dst] = True
                    stack.append(e.dst)
        return visited
