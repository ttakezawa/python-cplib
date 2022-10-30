from typing import Tuple

mod1000000007 = 1000000007
mod998244353 = 998244353


def pow_mod(x: int, n: int, mod: int) -> int:
    if mod == 1:
        return 0
    x %= mod
    r = 1
    while n:
        if n & 1:
            r = r * x % mod
        x = x * x % mod
        n >>= 1
    return r


def inv_mod(x: int, mod: int) -> int:
    """xとmodは互いに素 GCD(x,mod)=1 であることが必要。互いに素でない場合はxとmodをgcdで割っておくことを検討する"""
    assert 1 <= mod
    z = _inv_gcd(x, mod)
    if z[0] != 1:
        raise ValueError(f"GCD(f{x},f{mod})={z[0]}, but gcd must be 1")
    assert z[0] == 1
    return z[1]


def _inv_gcd(a: int, b: int) -> Tuple[int, int]:
    a %= b
    if a == 0:
        return b, 0
    s, t = b, a
    m0, m1 = 0, 1
    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u
        s, t = t, s
        m0, m1 = m1, m0
    if m0 < 0:
        m0 += b // s
    return s, m0


class FactorialCache:
    __slots__ = (
        "mod",
        "_val",
        "_inv",
    )

    def __init__(self, max: int, mod: int) -> None:
        self.mod = mod
        self._val = [1] * (max + 1)
        self._inv = [1] * (max + 1)
        for i in range(2, max + 1):
            self._val[i] = self._val[i - 1] * i % mod
        self._inv[max] = inv_mod(self._val[max], mod)
        for i in reversed(range(3, max + 1)):
            self._inv[i - 1] = self._inv[i] * i % mod

    def comb(self, n: int, k: int) -> int:
        if n < k:
            return 0
        return self._val[n] * self._inv[k] % self.mod * self._inv[n - k] % self.mod

    def factorial(self, n: int) -> int:
        return self._val[n]

    def inv_factorial(self, n: int) -> int:
        return self._inv[n]
