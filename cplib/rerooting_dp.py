from collections import deque
from typing import Callable, Deque, Generator, List, Tuple, TypeVar


class _Tree:
    def __init__(self, adj: List[List[int]], root: int):
        n = len(adj)
        self.adj = adj
        self.root = root
        self.children: List[List[int]] = [[] for _ in range(n)]
        self.parents = [-1] * n
        self.depth_to_nodes: List[List[int]] = [[] for _ in range(n)]

        seen = [False] * n
        seen[0] = True
        q: Deque[Tuple[int, int]] = deque()
        q.append((root, 0))
        while q:
            v, depth = q.popleft()
            self.depth_to_nodes[depth].append(v)
            for u in adj[v]:
                if seen[u]:
                    continue
                seen[u] = True
                self.children[v].append(u)
                self.parents[u] = v
                q.append((u, depth + 1))

    def traverse_top_down(self) -> Generator[int, None, None]:
        for nodes in self.depth_to_nodes:
            for v in nodes:
                yield v

    def traverse_bottom_up(self) -> Generator[int, None, None]:
        for nodes in self.depth_to_nodes[::-1]:
            for v in nodes:
                yield v


S = TypeVar("S")


def rerooting_dp(
    adj: List[List[int]],
    identity: S,
    merge: Callable[[S, S], S],
    f: Callable[[S, int, int], S],
    g: Callable[[S, int], S],
) -> List[S]:
    """
    dp[v] = g(merge(f(dp[c1],v,c1), f(dp[c2],v,c2), f(dp[c3],v,c3), ...), v)
    c1, c2, c3,...: children of v
    f: add_edge(s, from_, to)
    g: add_children(s, v)
    """

    root = 0
    N = len(adj)
    t = _Tree(adj, root)

    # DFS like
    lower = [identity] * N
    for v in t.traverse_bottom_up():
        for c in t.children[v]:
            lower[v] = merge(lower[v], f(lower[c], v, c))
        lower[v] = g(lower[v], v)

    # BFS like
    upper = [identity] * N
    for v in t.traverse_top_down():
        cc = t.children[v]

        dp_l = [identity]
        x = identity
        for c in cc:
            x = merge(x, f(lower[c], v, c))
            dp_l.append(x)

        dp_r = [identity]
        x = identity
        for c in cc[::-1]:
            x = merge(x, f(lower[c], v, c))
            dp_r.append(x)
        dp_r.reverse()

        for i, c in enumerate(cc):
            a = merge(dp_l[i], dp_r[i + 1])
            if v != root:
                b = merge(a, f(upper[v], v, t.parents[v]))
            else:
                b = a

            upper[c] = g(b, v)

    ret = [identity] * (N)
    for v in range(N):
        if v != root:
            a = f(upper[v], v, t.parents[v])
        else:
            a = identity

        for c in t.children[v]:
            a = merge(a, f(lower[c], v, c))
        ret[v] = g(a, v)
    return ret
