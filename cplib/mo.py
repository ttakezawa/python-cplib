# Problem
# - https://atcoder.jp/contests/abc174/tasks/abc174_f
# - https://atcoder.jp/contests/abc242/tasks/abc242_g
from math import ceil, sqrt
from typing import Callable, List, Optional, Sequence, Tuple, TypeVar

T = TypeVar("T")


def mo_solve(
    queries: Sequence[Sequence[int]],
    extend: Callable[[int], None],
    shrink: Callable[[int], None],
    mapping: Callable[[int], T],
) -> List[Optional[T]]:
    n = max(map(lambda q: q[1], queries))
    sz = max(1, ceil(n / sqrt(len(queries))))
    buckets: List[List[Tuple[int, int, int]]] = [[] for _ in range(n // sz + 1)]
    for id in range(len(queries)):
        buckets[queries[id][0] // sz].append((queries[id][0], queries[id][1], id))
    for i in range(len(buckets)):
        buckets[i].sort(key=lambda q: q[1], reverse=bool(i & 1))

    ans: List[Optional[T]] = [None] * len(queries)
    cl, cr = 0, 0
    for b in buckets:
        for l, r, id in b:
            while cr < r:
                extend(cr)
                cr += 1
            while l < cl:
                cl -= 1
                extend(cl)
            while r < cr:
                cr -= 1
                shrink(cr)
            while cl < l:
                shrink(cl)
                cl += 1
            ans[id] = mapping(id)
    return ans