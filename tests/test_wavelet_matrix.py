from unittest import TestCase

from cplib.wavelet_matrix import CompressedWaveletMatrix


class Test(TestCase):
    def test_wavelet_matrix(self) -> None:
        v = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
        cwm = CompressedWaveletMatrix(v)
        assert cwm.access(4) == 5
        assert cwm.rank(8, 9, 5) == 1
        assert cwm.rank(0, len(v), 9) == 3
        assert cwm.kth_smallest(1, 4, 2) == 4
        assert cwm.kth_largest(1, 5, 3) == 1
        assert cwm.range_freq(3, 10, 5, 7) == 3
        assert cwm.prev_val(4, 9, 5) == 2
        assert cwm.next_val(4, 9, 7) == 9
