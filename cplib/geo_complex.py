import cmath
import math
from typing import List


def dot_product(a: complex, b: complex):
    return a.real * b.real + a.imag * b.imag


def cross_product(a: complex, b: complex):
    return a.real * b.imag - a.imag * b.real


def _iszero(x: float):
    return math.isclose(x, 0, abs_tol=1e-15)


def ccw(a: complex, b: complex, c: complex):
    t = cross_product(b - a, c - a)
    if _iszero(t):
        return 0
    if t > 0:
        return 1
    return -1


class Arg:  # also known as phase
    def __init__(self, point: complex):
        self.point = point

    @property
    def x(self):
        return self.point.real

    @property
    def y(self):
        return self.point.imag

    @property
    def real(self):
        return self.point.real

    @property
    def imag(self):
        return self.point.imag

    def radians(self):
        return cmath.phase(self.point)

    def degrees(self):
        return math.degrees(self.radians())

    def area(self):
        return _area(self.point)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Arg):
            return NotImplemented
        return arg_cmp(self.point, other.point) == 0

    def __lt__(self, other: "Arg"):
        return arg_cmp(self.point, other.point) < 0

    def __ne__(self, other: object):
        return not self.__eq__(other)

    def __le__(self, other: "Arg"):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other: "Arg"):
        return not self.__le__(other)

    def __ge__(self, other: "Arg"):
        return not self.__lt__(other)


def arg_sort(points: List[complex]):
    from functools import cmp_to_key

    points.sort(key=cmp_to_key(arg_cmp))


def arg_cmp(p: complex, q: complex):
    pa, qa = _area(p), _area(q)
    if pa < qa:
        return -1
    elif pa > qa:
        return 1
    return -ccw(p, q, 0)


def _area(p: complex):
    x, y = p.real, p.imag
    xz, yz = _iszero(x), _iszero(y)
    if xz and yz:
        return 0
    if (x > 0 and not xz) and (y >= 0 or yz):  # x > 0 and y >= 0
        return 1
    if (x <= 0 or xz) and (y > 0 and not yz):  # x <= 0 and y > 0
        return 2
    if (x < 0 and not xz) and (y <= 0 or yz):  # x < 0 and y <= 0
        return 3
    return 4
