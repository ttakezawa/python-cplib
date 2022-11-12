# Originaged from https://github.com/not522/ac-library-python/blob/master/atcoder/dsu.py
from typing import Hashable, List


class DSUDict:
    def __init__(self) -> None:
        self._parent: dict[Hashable, Hashable] = {}
        self._size: dict[Hashable, int] = {}

    def add_node(self, a: Hashable):
        if a not in self._parent:
            self._parent[a] = a
            self._size[a] = 1

    def leader(self, a: Hashable) -> Hashable:
        self.add_node(a)
        buf: list[Hashable] = []
        while self._parent[a] != a:
            buf.append(a)
            a = self._parent[a]
        for l in buf:
            self._parent[l] = a
        return a

    def merge(self, a: Hashable, b: Hashable) -> Hashable:
        self.add_node(a)
        self.add_node(b)
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

    def same(self, a: Hashable, b: Hashable) -> bool:
        self.add_node(a)
        self.add_node(b)
        return self.leader(a) == self.leader(b)

    def size(self, a: Hashable) -> int:
        self.add_node(a)
        return self._size[self.leader(a)]

    def groups(self) -> List[List[Hashable]]:
        result: dict[Hashable, list[Hashable]] = {}
        for i in self._parent:
            rt = self.leader(i)
            if rt in result:
                result[rt].append(i)
            else:
                result[rt] = [i]
        return list(result.values())
