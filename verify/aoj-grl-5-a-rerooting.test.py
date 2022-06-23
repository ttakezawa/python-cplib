# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_A

from typing import Dict, List, Tuple
from cplib.rerooting_dp import rerooting_dp


def main():
    n = int(input())
    edges: Dict[Tuple[int, int], int] = dict()
    adj: List[List[int]] = [[] for _ in range(n)]
    for _ in range(n - 1):
        s, t, w = map(int, input().split())
        edges[(s, t)] = w
        edges[(t, s)] = w
        adj[s].append(t)
        adj[t].append(s)

    dp = rerooting_dp(
        adj,
        identity=0,
        merge=lambda x, y: max(x, y),
        add_edge=lambda s, src, dst: s + edges[(src, dst)],
        add_children=lambda s, v: s,
    )
    print(max(dp))


main()