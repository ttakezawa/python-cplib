from unittest import TestCase


from cplib.mo import mo_solve


class Test(TestCase):
    def test_mo(self) -> None:
        # https://atcoder.jp/contests/abc174/tasks/abc174_f
        c = [0, 1, 0, 2]
        queries = [(0, 3), (1, 4), (2, 3)]
        sum_ = [0] * 4
        cur = 0

        def extend(pos: int) -> None:
            nonlocal cur
            if sum_[c[pos]] == 0:
                cur += 1
            sum_[c[pos]] += 1

        def shrink(pos: int) -> None:
            nonlocal cur
            sum_[c[pos]] -= 1
            if sum_[c[pos]] == 0:
                cur -= 1

        def mapping(query_id: int) -> int:
            return cur

        ans = mo_solve(queries, extend, shrink, mapping)
        assert ans == [2, 3, 1]
