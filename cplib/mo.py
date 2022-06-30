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
    k = max(n, ceil(n / sqrt(len(queries))))

    queries = list(map(lambda iq: (iq[1][0], iq[1][1], iq[0]), enumerate(queries)))

    def keyfunc(q: Sequence[int]) -> Tuple[int, int]:
        return (q[0] // k, n - q[1] if (q[0] // k) & 1 else q[1])

    queries.sort(key=keyfunc)

    ans: List[Optional[T]] = [None] * len(queries)
    cl, cr = 0, 0
    for l, r, id in queries:
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
        v = mapping(id)
        ans[id] = v
    return ans