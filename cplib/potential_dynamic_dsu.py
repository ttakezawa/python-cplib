# Originaged from https://github.com/not522/ac-library-python/blob/master/atcoder/dsu.py
# Verify
# - https://onlinejudge.u-aizu.ac.jp/problems/DSL_1_B
# - https://atcoder.jp/contests/abc280/tasks/abc280_f
from typing import Generic, Hashable, List, TypeVar

_S = TypeVar("_S", bound=Hashable)


class PotentialDynamicDSU(Generic[_S]):
    def __init__(self) -> None:
        self._parent: dict[_S, _S] = {}
        self._size: dict[_S, int] = {}
        self._potential: dict[_S, int] = {}

    def leader(self, a: _S) -> _S:
        if a not in self._parent:
            # If a is not present, add as new node.
            self._parent[a] = a
            self._size[a] = 1
            self._potential[a] = 0
            return a
        cum = 0
        buf: list[_S] = []
        while self._parent[a] != a:
            buf.append(a)
            cum += self._potential[a]
            a = self._parent[a]
        for v in buf:
            self._potential[v], cum = cum, cum - self._potential[v]
            self._parent[v] = a
        return a

    def merge(self, a: _S, b: _S, diff: int) -> _S:
        """b is greater than a by diff: potential[b] = potential[a] + diff"""
        x = self.leader(a)
        y = self.leader(b)
        diff += self._potential[a] - self._potential[b]
        if x == y:
            return x
        if self._size[x] < self._size[y]:
            x, y, diff = y, x, -diff
        self._parent[y] = x
        self._size[x] += self._size[y]
        self._size[y] = self._size[x]
        self._potential[y] = diff
        return x

    def diff(self, a: _S, b: _S) -> int:
        """returns the difference between a and b. (diff(a,b) = potential[b] - potential[a])"""
        # leader should be called here
        if not self.same(a, b):
            raise ValueError(f"a and b ({a} and {b}) is not same group: ")
        return self._potential[b] - self._potential[a]

    def same(self, a: _S, b: _S) -> bool:
        return self.leader(a) == self.leader(b)

    def size(self, a: _S) -> int:
        return self._size[self.leader(a)]

    def groups(self) -> List[List[_S]]:
        result: dict[_S, list[_S]] = {}
        for i in self._parent:
            rt = self.leader(i)
            if rt in result:
                result[rt].append(i)
            else:
                result[rt] = [i]
        return list(result.values())
