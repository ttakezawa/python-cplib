from unittest import TestCase

from cplib.rolling_hash import RollingHash, longest_common_prefix


class Test(TestCase):
    def test_longest_common_prefix(self) -> None:
        rh1 = RollingHash("missisippi")
        rh2 = RollingHash("issiippi")

        assert longest_common_prefix(rh1, rh2, 0, 10, 0, 8) == 0
        assert longest_common_prefix(rh1, rh2, 1, 10, 0, 8) == 4  # [issi]
