# Originated from https://nebocco.hatenablog.com/entry/2021/11/13/185816
import math
from typing import List, Tuple, Union

Num = Union[int, float]
Point = Tuple[Num, Num]


class Arg:  # also known as phase
    def __init__(self, x: Num, y: Num):
        self.x, self.y = x, y

    def radians(self):
        return math.atan2(self.y, self.x)

    def degrees(self):
        return math.degrees(self.radians())

    def area(self):
        return area((self.x, self.y))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Arg):
            return NotImplemented
        return self.x * other.y == self.y * other.x

    def __lt__(self, other: "Arg"):
        return arg_cmp((self.x, self.y), (other.x, other.y)) < 0

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


def arg_cmp(p: Point, q: Point) -> int:
    pa, qa = area(p), area(q)
    if pa < qa:
        return -1
    elif pa > qa:
        return 1
    z = p[0] * q[1] - p[1] * q[0]
    if z > 0:
        return -1
    elif z < 0:
        return 1
    return 0


def area(p: Point) -> int:
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
