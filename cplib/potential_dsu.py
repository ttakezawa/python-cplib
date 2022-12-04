from typing import List


class PotentialDSU:
    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.parent_or_size = [-1] * n
        self._potential = [0] * n

    def merge(self, a: int, b: int, diff: int) -> int:
        """b is greater than a by diff: potential[b] = potential[a] + diff"""
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        x = self.leader(a)
        y = self.leader(b)
        diff += self._potential[a] - self._potential[b]

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y, diff = y, x, -diff

        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        self._potential[y] = diff

        return x

    def diff(self, a: int, b: int) -> int:
        """returns the difference between a and b. (diff(a,b) = potential[b] - potential[a])"""
        # leader should be called here
        if not self.same(a, b):
            raise ValueError(f"a and b ({a} and {b}) is not same group: ")
        return self._potential[b] - self._potential[a]

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        assert 0 <= a < self._n

        cum = 0
        leader = a
        while self.parent_or_size[leader] >= 0:
            cum += self._potential[leader]
            leader = self.parent_or_size[leader]
        while a != leader:
            self._potential[a], cum = cum, cum - self._potential[a]
            self.parent_or_size[a], a = leader, self.parent_or_size[a]
        return leader

    def size(self, a: int) -> int:
        assert 0 <= a < self._n

        return -self.parent_or_size[self.leader(a)]

    def groups(self) -> List[List[int]]:
        leader_buf = [self.leader(i) for i in range(self._n)]

        result: List[List[int]] = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)

        return list(filter(lambda r: r, result))
