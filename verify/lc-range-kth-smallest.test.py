# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_kth_smallest
import sys

from cplib.wavelet_matrix import CompressedWaveletMatrix


def input() -> bytes:
    return sys.stdin.buffer.readline()


def main():
    _, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(q)]

    cwm = CompressedWaveletMatrix(a)
    ans = []
    for l, r, k in queries:
        ans.append(cwm.kth_smallest(l, r, k))
    print("\n".join(map(str, ans)))


main()
