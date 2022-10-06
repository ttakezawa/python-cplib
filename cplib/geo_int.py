import math
from typing import List, Tuple

Point = Tuple[int, int]


def dot_product(a: Point, b: Point):
    return a[0] * b[0] + a[1] * b[1]


def cross_product(a: Point, b: Point):
    return a[0] * b[1] - a[1] * b[0]


def ccw(a: Point, b: Point, c: Point):
    t = cross_product((b[0] - a[0], b[1] - a[1]), (c[0] - a[0], c[1] - a[1]))
    if t > 0:
        return 1
    elif t < 0:
        return -1
    return 0


class Arg:  # also known as phase
    def __init__(self, p: Point):
        self.point = p

    @property
    def x(self):
        return self.point[0]

    @property
    def y(self):
        return self.point[1]

    def radians(self):
        return math.atan2(self.point[0], self.point[1])

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


def arg_sort(points: List[Point]):
    from functools import cmp_to_key

    points.sort(key=cmp_to_key(arg_cmp))


def arg_cmp(p: Point, q: Point):
    pa, qa = _area(p), _area(q)
    if pa < qa:
        return -1
    elif pa > qa:
        return 1
    return -ccw(p, q, (0, 0))


def _area(p: Point):
    x, y = p[0], p[1]
    if x == 0 and y == 0:
        return 0
    if x > 0 and y >= 0:
        return 1
    if x <= 0 and y > 0:
        return 2
    if x < 0 and y <= 0:
        return 3
    return 4
