# Originated from https://qiita.com/keymoon/items/11fac5627672a6d6a9f6
# Verify https://atcoder.jp/contests/abc284/tasks/abc284_f
from random import choice

BASE = 10**9 + choice([5, 8, 9, 10, 14, 27, 29, 44, 61, 62, 65, 66, 70, 81, 84, 85])
MODULO = (1 << 61) - 1
POWS = [1]

_MASK30 = (1 << 30) - 1
_MASK31 = (1 << 31) - 1
_MASK61 = (1 << 61) - 1


def _mul(a: int, b: int):
    """returns a * b % MODULO"""
    au = a >> 31
    ad = a & _MASK31
    bu = b >> 31
    bd = b & _MASK31
    mid = ad * bu + au * bd
    x = au * bu * 2 + (mid >> 30) + ((mid & _MASK30) << 31) + ad * bd
    return ((x >> 61) + (x & _MASK61)) % MODULO


def _mod(x: int):
    """returns x % MODULO"""
    return ((x >> 61) + (x & _MASK61)) % MODULO


class RollingHash:
    def __init__(self, string: str):
        """O(|S|)"""
        hashes = [0]
        for c in string:
            nxt = _mod(_mul(hashes[-1], BASE) + ord(c))
            hashes.append(nxt)
        self.hashes = hashes
        self.string = string

    def hash(self, l: int, r: int):
        """calculate hash of string[l:r]. O(1)"""
        while len(POWS) <= r - l:
            POWS.append(_mul(POWS[-1], BASE))
        return _mod(self.hashes[r] - _mul(self.hashes[l], POWS[r - l]))

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
    return _mod(_mul(hash1, POWS[hash2_len]) + hash2)


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
