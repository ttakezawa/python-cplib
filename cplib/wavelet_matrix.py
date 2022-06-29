# Originated from https://github.com/Neterukun1993/Library/blob/master/DataStructure/Wavelet/WaveletMatrix.py
from bisect import bisect_left
from typing import List, Optional
from array import array


class BitVector:
    __slots__ = ("block_num", "bit", "cnt")

    def __init__(self, size: int):
        self.block_num = (size + 31) >> 5
        self.bit = array("l", [0] * self.block_num)
        self.cnt = array("l", [0] * self.block_num)

    def __getitem__(self, i: int) -> int:
        return (self.bit[i >> 5] >> (i & 31)) & 1

    def set(self, i: int) -> None:
        self.bit[i >> 5] |= 1 << (i & 31)

    def build(self) -> None:
        for i in range(self.block_num - 1):
            self.cnt[i + 1] = self.cnt[i] + _popcnt(self.bit[i])

    def access(self, i: int) -> int:
        return (self.bit[i >> 5] >> (i & 31)) & 1

    def rank0(self, r: int) -> int:
        return r - self.cnt[r >> 5] - _popcnt(self.bit[r >> 5] & ((1 << (r & 31)) - 1))

    def rank1(self, r: int) -> int:
        return self.cnt[r >> 5] + _popcnt(self.bit[r >> 5] & ((1 << (r & 31)) - 1))


class WaveletMatrix:
    __slots__ = ("maxlog", "n", "mat", "zs")

    def __init__(self, array: List[int], MAXLOG: int = 32):
        self.maxlog = MAXLOG
        self.n = len(array)
        self.mat: List[BitVector] = []
        self.zs: List[int] = []

        for d in reversed(range(self.maxlog)):
            vec = BitVector(self.n + 1)
            ls: List[int] = []
            rs: List[int] = []
            for i, val in enumerate(array):
                if (val >> d) & 1:
                    rs.append(val)
                    vec.set(i)
                else:
                    ls.append(val)
            vec.build()
            self.mat.append(vec)
            self.zs.append(len(ls))
            array = ls + rs

    def access(self, i: int) -> int:
        res = 0
        for d in range(self.maxlog):
            res <<= 1
            if self.mat[d][i]:
                res |= 1
                i = self.mat[d].rank1(i) + self.zs[d]
            else:
                i = self.mat[d].rank0(i)
        return res

    def rank(self, l: int, r: int, val: int) -> int:
        for d in range(self.maxlog):
            if val >> (self.maxlog - d - 1) & 1:
                l = self.mat[d].rank1(l) + self.zs[d]
                r = self.mat[d].rank1(r) + self.zs[d]
            else:
                l = self.mat[d].rank0(l)
                r = self.mat[d].rank0(r)
        return r - l

    def quantile(self, l: int, r: int, k: int) -> int:
        res = 0
        for d in range(self.maxlog):
            res <<= 1
            cntl, cntr = self.mat[d].rank0(l), self.mat[d].rank0(r)
            if k >= cntr - cntl:
                l = self.mat[d].rank1(l) + self.zs[d]
                r = self.mat[d].rank1(r) + self.zs[d]
                res |= 1
                k -= cntr - cntl
            else:
                l = cntl
                r = cntr
        return res

    def kth_smallest(self, l: int, r: int, k: int) -> int:
        return self.quantile(l, r, k)

    def kth_largest(self, l: int, r: int, k: int) -> int:
        return self.quantile(l, r, r - l - k - 1)

    def _range_freq(self, l: int, r: int, upper: int) -> int:
        res = 0
        for d in range(self.maxlog):
            if upper >> (self.maxlog - d - 1) & 1:
                res += self.mat[d].rank0(r) - self.mat[d].rank0(l)
                l = self.mat[d].rank1(l) + self.zs[d]
                r = self.mat[d].rank1(r) + self.zs[d]
            else:
                l = self.mat[d].rank0(l)
                r = self.mat[d].rank0(r)
        return res

    def range_freq(self, l: int, r: int, lower: int, upper: int) -> int:
        return self._range_freq(l, r, upper) - self._range_freq(l, r, lower)

    def prev_val(self, l: int, r: int, upper: int) -> Optional[int]:
        cnt = self._range_freq(l, r, upper)
        return None if cnt == 0 else self.kth_smallest(l, r, cnt - 1)

    def next_val(self, l: int, r: int, lower: int) -> Optional[int]:
        cnt = self._range_freq(l, r, lower)
        return None if cnt == r - l else self.kth_smallest(l, r, cnt)


class CompressedWaveletMatrix:
    __slots__ = ("vals", "comp", "wm")

    def __init__(self, array: List[int]):
        self.vals = sorted(set(array))
        self.comp = {val: idx for idx, val in enumerate(self.vals)}
        array = [self.comp[val] for val in array]
        self.wm = WaveletMatrix(array, len(self.vals).bit_length())

    def access(self, i: int) -> int:
        return self.vals[self.wm.access(i)]

    def rank(self, l: int, r: int, val: int) -> int:
        return self.wm.rank(l, r, self.comp[val]) if val in self.comp else 0

    def kth_smallest(self, l: int, r: int, k: int) -> int:
        return self.vals[self.wm.kth_smallest(l, r, k)]

    def kth_largest(self, l: int, r: int, k: int) -> int:
        return self.vals[self.wm.kth_largest(l, r, k)]

    def range_freq(self, l: int, r: int, lower: int, upper: int) -> int:
        lower = bisect_left(self.vals, lower)
        upper = bisect_left(self.vals, upper)
        return self.wm.range_freq(l, r, lower, upper)

    def prev_val(self, l: int, r: int, upper: int) -> Optional[int]:
        upper = bisect_left(self.vals, upper)
        res = self.wm.prev_val(l, r, upper)
        return None if res is None else self.vals[res]

    def next_val(self, l: int, r: int, lower: int) -> Optional[int]:
        lower = bisect_left(self.vals, lower)
        res = self.wm.next_val(l, r, lower)
        return None if res is None else self.vals[res]


def _popcnt(x: int) -> int:
    x = x - ((x >> 1) & 0x55555555)
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
    x = (x + (x >> 4)) & 0x0F0F0F0F
    x = x + (x >> 8)
    x = x + (x >> 16)
    return x & 0x3F
