# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca
import sys
from typing import List
from cplib.lca import LCAGraph


def input() -> bytes:
    return sys.stdin.buffer.readline()


def main():
    n, q = map(int, input().split())
    p = [int(x) for x in input().split()]
    adj: List[List[int]] = [[] for _ in range(n)]
    for i, pp in enumerate(p):
        i += 1
        adj[i].append(pp)
        adj[pp].append(i)
    g = LCAGraph(adj)
    for _ in range(q):
        u, v = map(int, input().split())
        print(g.lca(u, v))


main()