BASE = 257  # 37, 257, 1002, 3001, 10001, 1000000001
MODULO = (1 << 61) - 1
POWS = [1]


class RollingHash:
    def __init__(self, string: str):
        """O(|S|)"""
        hashes = [0]
        for c in string:
            val = ord(c)
            nxt = hashes[-1] * BASE + val
            hashes.append(nxt % MODULO)
        self.hashes = hashes

    def hash(self, l: int, r: int):
        """calculate hash of string[l:r]. O(1)"""
        while len(POWS) <= r - l:
            POWS.append(POWS[-1] * BASE % MODULO)
        return (self.hashes[r] - self.hashes[l] * POWS[r - l]) % MODULO


def hash(string: str):
    """calculate hash of string. O(|S|)"""
    return RollingHash(string).hash(0, len(string))


def longest_common_prefix(
    rolling_hash1: RollingHash,
    rolling_hash2: RollingHash,
    l1: int,
    r1: int,
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
