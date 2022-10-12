from unittest import TestCase

from cplib.suffix_array import build_suffix_array, find_all


class Test(TestCase):
    def test_suffix_array(self) -> None:
        s = "missisippi"
        sa = build_suffix_array(s)

        expected = [
            "i",
            "ippi",
            "isippi",
            "issisippi",
            "missisippi",
            "pi",
            "ppi",
            "sippi",
            "sisippi",
            "ssisippi",
        ]

        for i in range(len(sa)):
            assert expected[i] == s[sa[i] :]

    def test_find_all(self) -> None:
        s = "missisippi"
        sa = build_suffix_array(s)
        assert find_all(s, sa, "") == [9, 6, 4, 1, 0, 8, 7, 5, 3, 2]
        assert find_all(s, sa, "i") == [9, 6, 4, 1]
        assert find_all(s, sa, "is") == [4, 1]
        assert find_all(s, sa, "ssi") == [2]
        assert find_all(s, sa, "ssp") == []
        assert find_all(s, sa, "zzzzzzzzzzzzzzzz") == []
