from unittest import TestCase

from cplib.matrix import Matrix


class Test(TestCase):
    def test_identity(self) -> None:
        identity = Matrix.identity(3)
        assert identity == Matrix.from_list([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    def test_iter(self) -> None:
        x = Matrix.from_list([[1, 2], [3, 4]])
        it = iter(x)
        assert next(it) == [1, 2]
        assert next(it) == [3, 4]
        with self.assertRaises(StopIteration):
            next(it)

    def test_get_column(self) -> None:
        x = Matrix.from_list([[1, 2], [3, 4]])
        assert x.get_column(0) == [1,3]
        assert x.get_column(1) == [2,4]

    def test_size(self) -> None:
        x = Matrix.from_list([[1, 2, 3], [3, 4, 5]])
        assert x.rows() == 2
        assert x.cols() == 3

    def test_add(self) -> None:
        x, y = Matrix.from_list([[1, 2], [3, 4]]), Matrix.from_list([[0, 4], [2, 1]])
        assert x + y == Matrix.from_list([[1, 6], [5, 5]])
        x += y
        assert x == Matrix.from_list([[1, 6], [5, 5]])

    def test_sub(self) -> None:
        x, y = Matrix.from_list([[1, 2], [3, 4]]), Matrix.from_list([[0, 4], [2, 1]])
        assert x - y == Matrix.from_list([[1, -2], [1, 3]])
        x -= y
        assert x == Matrix.from_list([[1, -2], [1, 3]])

    def test_neg(self) -> None:
        x = Matrix.from_list([[1, 2], [3, 4]])
        assert -x == Matrix.from_list([[-1, -2], [-3, -4]])

    def test_mod(self) -> None:
        x = Matrix.from_list([[1, 2], [3, 4]])
        assert x % 3 == Matrix.from_list([[1, 2], [0, 1]])
        x %= 3
        assert x == Matrix.from_list([[1, 2], [0, 1]])

    def test_mul(self) -> None:
        x, y = Matrix.from_list([[1, 2], [3, 4]]), Matrix.from_list([[0, 4], [2, 1]])
        assert x * y == Matrix.from_list([[4, 6], [8, 16]])
        x *= y
        assert x == Matrix.from_list([[4, 6], [8, 16]])

    def test_pow(self) -> None:
        x = Matrix.from_list([[1, 2], [3, 4]])
        x10 = Matrix.identity(2)
        for _ in range(10):  # naive calculation
            x10 *= x
        assert x ** 10 == x10
        x **= 10
        assert x == x10

    def test_pow_mod(self) -> None:
        x = Matrix.from_list([[1, 2], [3, 4]])
        x100 = Matrix.identity(2)
        for _ in range(100):  # naive calculation
            x100 *= x
            x100 %= 1223
        assert x.pow_mod(100, 1223) == x100
        assert x == Matrix.from_list([[1, 2], [3, 4]])
