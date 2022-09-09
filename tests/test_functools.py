from unittest import TestCase

from cplib.functools import bootstrap_with_memo


class Test(TestCase):
    def test_bootstrap_with_memo(self) -> None:
        @bootstrap_with_memo
        def fib(n):
            if n <= 1:
                yield n
            a = yield fib(n - 1)
            b = yield fib(n - 2)
            yield a + b

        assert fib(3) == 2
        assert fib(3) == 2
        assert fib(4) == 3
        assert fib(2) == 1
        assert fib(50) == 12586269025
