# Originated from
# - https://null-mn.hatenablog.com/entry/2020/04/14/124151
# - https://algo-logic.info/tree-dp/

from typing import Callable, List, Tuple, TypeVar


class _Tree:
    from typing import Generator

    def __init__(self, adj: List[List[int]], root: int):
        import collections
        from typing import Deque

        n = len(adj)
        self.adj = adj
        self.root = root
        self.children: List[List[int]] = [[] for _ in range(n)]
        self.parents = [-1] * n
        self.depth_to_nodes: List[List[int]] = [[] for _ in range(n)]

        seen = [False] * n
        seen[0] = True

        q: Deque[Tuple[int, int]] = collections.deque()
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


_S = TypeVar("_S")


def rerooting_dp(
    adj: List[List[int]],
    identity: _S,
    merge: Callable[[_S, _S], _S],
    add_edge: Callable[[_S, int, int], _S],
    add_children: Callable[[_S, int], _S],
) -> List[_S]:
    """全方位木DP

    Example::

        dp = rerooting_dp(
            adj,
            identity=0,
            merge=lambda x, y: max(x, y),
            add_edge=lambda x, src, dst: s + edges[(src, dst)],
            add_children=lambda x, v: s,
        )

    Description:

        dp[v] = g(merge(f(dp[c1],v,c1), f(dp[c2],v,c2), f(dp[c3],v,c3), ...), v)
        c1, c2, c3,...: children of v

    Args:

        add_edge: f(x, src, dst)
        add_children: g(x, v)
    """
    f, g = add_edge, add_children
    root = 0
    N = len(adj)
    t = _Tree(adj, root)

    # DFS
    lower = [identity] * N
    for v in t.traverse_bottom_up():
        for c in t.children[v]:
            lower[v] = merge(lower[v], f(lower[c], v, c))
        lower[v] = g(lower[v], v)

    # BFS
    upper = [identity] * N
    for v in t.traverse_top_down():
        cc = t.children[v]

        dp_l = [identity] * (len(cc) + 1)
        for i in range(len(cc)):
            dp_l[i + 1] = merge(dp_l[i], f(lower[cc[i]], v, cc[i]))
        dp_r = [identity] * (len(cc) + 1)
        for i in range(len(cc) - 1, 0, -1):
            dp_r[i] = merge(dp_r[i + 1], f(lower[cc[i]], v, cc[i]))

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
