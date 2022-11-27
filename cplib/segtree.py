# Originated from: https://github.com/not522/ac-library-python/blob/master/atcoder/segtree.py
from typing import Callable, Generic, List, TypeVar

_S = TypeVar("_S")


class Segtree(Generic[_S]):
    __slots__ = (
        "_op",
        "_e",
        "_n",
        "_log",
        "_size",
        "_d",
    )

    def __init__(
        self,
        v: List[_S],
        op: Callable[[_S, _S], _S],
        e: _S,
    ) -> None:
        """
        Examples::

            Segtree(v, 0, math_backport.gcd)
            Segtree(v, 0, operator.add)
            Segtree(v, -inf, max)
            Segtree(v, inf, min)
        """
        self._op = op
        self._e = e

        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._d[i] = self._op(self._d[2 * i], self._d[2 * i + 1])

    def set(self, p: int, x: _S) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            k = p >> i
            self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def get(self, p: int) -> _S:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod_range(self, left: int, right: int) -> _S:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> _S:
        return self._d[1]

    def max_right(self, left: int, f: Callable[[_S], bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int, f: Callable[[_S], bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def __len__(self) -> int:
        return self._n

    def __getitem__(self, key: int) -> _S:
        return self.get(key)

    def add(self, p: int, increment: _S) -> None:
        self.set(p, self.get(p) + increment)  # type: ignore

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self._d[self._size:self._size+self._n].__str__()}>"


def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1

    return x
