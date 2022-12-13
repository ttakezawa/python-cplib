from unittest import TestCase

from cplib.rolling_hash import RollingHash, longest_common_prefix


class Test(TestCase):
    def test_longest_common_prefix(self) -> None:
        rh1 = RollingHash("missisippi")
        rh2 = RollingHash("issiippi")

        assert longest_common_prefix(rh1, 0, 10, rh2, 0, 8) == 0
        assert longest_common_prefix(rh1, 1, 10, rh2, 0, 8) == 4  # [issi]

    def test_find(self) -> None:
        s = "missisippi"
        rh = RollingHash(s)
        for i in range(len(s)):
            # RollingHash.find behaves similarity to str.find
            assert rh.find("si", i) == s.find("si", i)
