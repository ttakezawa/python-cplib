from typing import List, Tuple


def build_dist(adj: List[List[int]], src: int) -> List[int]:
    dists = [-1] * len(adj)
    dists[src] = 0
    st = [src]
    while st:
        v = st.pop()
        for u in adj[v]:
            if dists[u] >= 0:
                continue
            dists[u] = dists[v] + 1
            st.append(u)
    return dists


def diameter(adj: List[List[int]]) -> Tuple[int, int, List[int]]:
    """returns Tuple of (farthest pair, path of diameter)"""
    A, _ = find_farthest(adj, 0)
    B, backs = find_farthest(adj, A)
    path = [B]
    v = B
    while v != A:
        v = backs[v]
        path.append(v)
    path.reverse()
    return A, B, path


def find_farthest(adj: List[List[int]], src: int) -> Tuple[int, List[int]]:
    """returns tuple of (farthest vertex, backs)"""
    backs = [-1] * len(adj)
    dists = [-1] * len(adj)
    dists[src] = 0
    farthest = src
    st = [src]
    while st:
        v = st.pop()
        for u in adj[v]:
            if dists[u] >= 0:
                continue
            dists[u] = dists[v] + 1
            backs[u] = v
            if dists[u] > dists[farthest]:
                farthest = u
            st.append(u)
    return farthest, backs
