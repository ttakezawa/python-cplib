# Originaged from https://github.com/not522/ac-library-python/blob/master/atcoder/dsu.py
from typing import Generic, Hashable, List, TypeVar

_S = TypeVar("_S", bound=Hashable)


class DSUDict(Generic[_S]):
    def __init__(self) -> None:
        self._parent: dict[_S, _S] = {}
        self._size: dict[_S, int] = {}

    def leader(self, a: _S) -> _S:
        if a not in self._parent:
            # If a is not present, add as new node.
            self._parent[a] = a
            self._size[a] = 1
            return a
        buf: list[_S] = []
        while self._parent[a] != a:
            buf.append(a)
            a = self._parent[a]
        for l in buf:
            self._parent[l] = a
        return a

    def merge(self, a: _S, b: _S) -> _S:
        x = self.leader(a)
        y = self.leader(b)
        if x == y:
            return x
        if self._size[x] < self._size[y]:
            x, y = y, x
        self._parent[y] = x
        self._size[x] += self._size[y]
        self._size[y] = self._size[x]
        return x

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
