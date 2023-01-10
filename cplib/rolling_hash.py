# Originated from https://qiita.com/keymoon/items/11fac5627672a6d6a9f6
# Verify
# - https://atcoder.jp/contests/abc284/tasks/abc284_f
# - https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bd
from random import choice

_MASK30 = (1 << 30) - 1
_MASK31 = (1 << 31) - 1
_MASK61 = (1 << 61) - 1

BASE = 10**9 + choice([5, 8, 9, 10, 14, 27, 29, 44, 61, 62, 65, 66, 70, 81, 84, 85])
MODULO = _MASK61
POWS = [1]


def _mul(a: int, b: int):
    """Return a * b ≡ MODULO"""
    au, ad = a >> 31, a & _MASK31
    bu, bd = b >> 31, b & _MASK31
    mid = ad * bu + au * bd
    return ((au * bu) << 1) + ad * bd + ((mid & _MASK30) << 31) + (mid >> 30)


class RollingHash:
    def __init__(self, string: str):
        """O(|S|)"""
        hashes = [0]
        for c in string:
            hashes.append((_mul(hashes[-1], BASE) + ord(c)) % MODULO)
        self.hashes = hashes
        self.string = string

    def hash(self, l: int, r: int):
        """calculate hash of string[l:r]. O(1)"""
        while len(POWS) <= r - l:
            POWS.append(_mul(POWS[-1], BASE))
        return (self.hashes[r] - _mul(self.hashes[l], POWS[r - l])) % MODULO

    def find(self, sub: str, start: int = 0) -> int:
        """O(|S|). Return the lowest index in the string where substring sub is found within the slice s[start:]. Return -1 if sub is not found."""
        h = hash(sub)
        for i in range(start, len(self.string) - len(sub) + 1):
            if h == self.hash(i, i + len(sub)):
                return i
        return -1


def connect(hash1: int, hash2: int, hash2_len: int):
    """O(1)"""
    while len(POWS) <= hash2_len:
        POWS.append(_mul(POWS[-1], BASE))
    return (_mul(hash1, POWS[hash2_len]) + hash2) % MODULO


def hash(string: str):
    """calculate hash of string. O(|S|)"""
    return RollingHash(string).hash(0, len(string))


def longest_common_prefix(
    rolling_hash1: RollingHash,
    l1: int,
    r1: int,
    rolling_hash2: RollingHash,
    l2: int,
    r2: int,
):
    """rh1の区間[l1,r1)とrh2の区間[l2,r2)の文字列で、最長共通接頭辞の長さを求める。O(log(|S|+|T|))"""
    ok, ng = 0, min(r1 - l1, r2 - l2) + 1
    while ng - ok > 1:
        med = ok + ng >> 1
        if rolling_hash1.hash(l1, l1 + med) == rolling_hash2.hash(l2, l2 + med):
            ok = med
        else:
            ng = med
    return ok
