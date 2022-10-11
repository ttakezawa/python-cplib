from unittest import TestCase

from cplib.suffix_array import build_suffix_array


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
