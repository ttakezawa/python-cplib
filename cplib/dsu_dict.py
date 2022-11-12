# Originaged from https://github.com/not522/ac-library-python/blob/master/atcoder/dsu.py
from typing import Dict, List


class DSUDict:
    def __init__(self) -> None:
        self.parent_or_size: dict[int, int] = {}

    def leader(self, a: int) -> int:
        L: list[int] = []
        while self.parent_or_size[a] >= 0:
            L.append(a)
            a = self.parent_or_size[a]
        for l in L:
            self.parent_or_size[l] = a
        return a

    def add_node(self, a: int):
        if a not in self.parent_or_size:
            self.parent_or_size[a] = -1

    def merge(self, a: int, b: int) -> int:
        self.add_node(a)
        self.add_node(b)
        x = self.leader(a)
        y = self.leader(b)
        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        return x

    def same(self, a: int, b: int) -> bool:
        self.add_node(a)
        self.add_node(b)
        return self.leader(a) == self.leader(b)

    def size(self, a: int) -> int:
        self.add_node(a)
        return -self.parent_or_size[self.leader(a)]

    def groups(self) -> Dict[int, List[int]]:
        result: Dict[int, List[int]] = {}
        for i in self.parent_or_size:
            rt = self.leader(i)
            if rt in result:
                result[rt].append(i)
            else:
                result[rt] = [i]
        return result
