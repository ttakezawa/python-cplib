# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_kth_smallest
import sys

from cplib.wavelet_matrix import CompressedWaveletMatrix


def input() -> bytes:
    return sys.stdin.buffer.readline()


def main():
    _n, q = map(int, input().split())
    a = [int(x) for x in input().split()]
    cwm = CompressedWaveletMatrix(a)
    for _ in range(q):
        a, b, c = map(int, input().split())
        print(cwm.kth_smallest(a, b, c))


main()
