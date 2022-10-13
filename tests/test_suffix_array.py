from unittest import TestCase

from cplib.suffix_array import build_lcp_array, build_suffix_array, contain, find_all


class Test(TestCase):
    def test_suffix_array(self) -> None:
        s = "missisippi"
        sa = build_suffix_array(s)

        assert sa == [9, 6, 4, 1, 0, 8, 7, 5, 3, 2]

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

    def test_lcp_array(self) -> None:
        s = "missisippi"
        sa = build_suffix_array(s)
        lcp = build_lcp_array(s, sa)
        assert lcp == [1, 1, 2, 0, 0, 1, 0, 2, 1]

    def test_find_all(self) -> None:
        s = "missisippi"
        sa = build_suffix_array(s)
        assert find_all(s, sa, "") == (0, 10)
        assert find_all(s, sa, "i") == (0, 4)
        assert find_all(s, sa, "is") == (2, 4)
        assert find_all(s, sa, "ssi") == (9, 10)
        assert find_all(s, sa, "ssp") == (10, 10)
        assert find_all(s, sa, "aaaaaaaaaaaaaaaa") == (0, 0)
        assert find_all(s, sa, "zzzzzzzzzzzzzzzz") == (10, 10)

    def test_contain(self) -> None:
        s = "missisippi"
        sa = build_suffix_array(s)
        assert contain(s, sa, "")
        assert contain(s, sa, "i")
        assert contain(s, sa, "is")
        assert contain(s, sa, "ssi")
        assert contain(s, sa, "ssp") == False
        assert contain(s, sa, "aaaaaaaaaaaaaaaa") == False
        assert contain(s, sa, "zzzzzzzzzzzzzzzz") == False
