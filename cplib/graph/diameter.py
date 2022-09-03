from typing import List, Tuple


def diameter(adj: List[List[int]]) -> Tuple[int, int]:
    _, A = dist(adj, 0)
    _, B = dist(adj, A)
    return A, B


def dist(adj: List[List[int]], src: int) -> Tuple[List[int], int]:
    """returns tuple of (dists, vertex such that the distance from src is maximized.)"""
    dists = [-1] * len(adj)
    dists[src] = 0
    st = [src]
    while st:
        v = st.pop()
        for u in adj[v]:
            if dists[u] == -1:
                dists[u] = dists[v] + 1
                st.append(u)
    max_vertex = src
    for i in range(len(adj)):
        if dists[i] > dists[max_vertex]:
            max_vertex = i
    return dists, max_vertex
