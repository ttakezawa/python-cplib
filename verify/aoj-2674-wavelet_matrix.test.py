# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2674
import sys

from cplib.wavelet_matrix import CompressedWaveletMatrix


def input() -> bytes:
    return sys.stdin.buffer.readline()


def main() -> None:
    n = int(input())
    x = list(map(int, input().split()))
    for i in range(n):
        x[i] += 10_000_000

    matrix = CompressedWaveletMatrix(x)
    q = int(input())
    for _ in range(q):
        l, r, e = map(int, input().split())

        l -= 1
        l1 = min(matrix.access(l), matrix.access(r - 1)) - e
        r1 = max(matrix.access(l), matrix.access(r - 1)) + e + 1
        ans = r - l - matrix.range_freq(l, r, l1, r1)
        print(ans)


main()
