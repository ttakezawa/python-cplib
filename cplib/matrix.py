from typing import Iterator, List, Union


class Matrix:
    __slots__ = "_inner"

    def __init__(self, n: int, m: int, default: int = 0) -> None:
        self._inner = [[default] * m for _ in range(n)]

    def __getitem__(self, row_idx: int) -> List[int]:
        return self._inner[row_idx]

    def __setitem__(self, row_idx: int, row: List[int]) -> None:
        assert self.cols() == len(row)
        self._inner[row_idx] = row

    def __iter__(self) -> Iterator[List[int]]:
        return self._inner.__iter__()

    def get_column(self, col_idx: int) -> List[int]:
        assert col_idx < self.cols()
        return [row[col_idx] for row in self]

    @classmethod
    def from_list(cls, lists: List[List[int]]) -> "Matrix":
        n = len(lists)
        m = len(lists[0])
        for i in range(1, n):
            assert len(lists[i]) == m
        mat = Matrix(0, 0)
        mat._inner = lists
        return mat

    @classmethod
    def identity(cls, n: int) -> "Matrix":
        e = Matrix(n, n)
        for i in range(n):
            e._inner[i][i] = 1
        return e

    def __str__(self) -> str:
        return self._inner.__str__()

    def rows(self) -> int:
        return len(self._inner)

    def cols(self) -> int:
        return len(self._inner[0])

    def copy(self) -> "Matrix":
        ret = Matrix(0, 0)
        ret._inner = [r.copy() for r in self._inner]
        return ret

    def _replace(self, other: "Matrix") -> None:
        for i in range(self.rows()):
            for j in range(self.cols()):
                self._inner[i][j] = other._inner[i][j]

    def __eq__(self, other: "object") -> bool:
        if not isinstance(other, Matrix):
            return False
        if not (self.rows() == other.rows() and self.cols() == other.cols()):
            return False
        for i in range(self.rows()):
            for j in range(self.cols()):
                if self._inner[i][j] != other._inner[i][j]:
                    return False
        return True

    def __add__(self, other: "Matrix") -> "Matrix":
        ret = self.copy()
        ret += other
        return ret

    def __iadd__(self, other: "Matrix") -> "Matrix":
        assert self.rows() == other.rows() and self.cols() == other.cols()
        for i in range(self.cols()):
            for j in range(self.rows()):
                self._inner[i][j] += other._inner[i][j]
        return self

    def __sub__(self, other: "Matrix") -> "Matrix":
        ret = self.copy()
        ret -= other
        return ret

    def __isub__(self, other: "Matrix") -> "Matrix":
        assert self.rows() == other.rows() and self.cols() == other.cols()
        for i in range(self.cols()):
            for j in range(self.rows()):
                self._inner[i][j] -= other._inner[i][j]
        return self

    def __neg__(self) -> "Matrix":
        return Matrix.from_list(
            [
                [-self._inner[i][j] for j in range(self.cols())]
                for i in range(self.rows())
            ]
        )

    def __mod__(self, other: int) -> "Matrix":
        ret = self.copy()
        ret %= other
        return ret

    def __imod__(self, mod: int) -> "Matrix":
        for i in range(self.cols()):
            for j in range(self.rows()):
                self._inner[i][j] %= mod
        return self

    def __mul__(self, other: Union["Matrix", int]) -> "Matrix":
        """O(n³)"""
        if isinstance(other, int):
            return Matrix.from_list(
                [
                    [self._inner[i][j] * other for j in range(self.cols())]
                    for i in range(self.rows())
                ]
            )

        h, w = self.rows(), self.cols()
        u, v = other.rows(), other.cols()
        assert w == u
        ret = Matrix(h, v)
        for i in range(h):
            for k in range(w):
                for j in range(v):
                    ret._inner[i][j] += self._inner[i][k] * other._inner[k][j]
        return ret

    def __imul__(self, other: Union["Matrix", int]) -> "Matrix":
        self._replace(self * other)
        return self

    def __pow__(self, exp: int) -> "Matrix":
        assert self.cols() == self.rows()
        base = self.copy()
        ret = Matrix.identity(self.cols())
        while exp:
            if exp & 1:
                ret *= base
            base *= base
            exp >>= 1
        return ret

    def __ipow__(self, exp: int) -> "Matrix":
        self._replace(self ** exp)
        return self

    def pow_mod(self, exp: int, mod: int) -> "Matrix":
        """self^exp % mod with O(n³log(exp))"""
        assert self.cols() == self.rows()
        base = self.copy()
        ret = Matrix.identity(self.cols())
        while exp:
            if exp & 1:
                ret *= base
                ret %= mod
            base *= base
            base %= mod
            exp >>= 1
        return ret
