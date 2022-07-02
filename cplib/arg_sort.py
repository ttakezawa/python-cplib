from functools import cmp_to_key
from typing import List, Tuple, Union

Num = Union[int, float]
Point = Tuple[Num, Num]


def arg_sort(points: List[Point]):
    points.sort(key=cmp_to_key(arg_cmp))


def area(p: Point) -> int:
    x, y = p[0], p[1]
    if x == 0 and y == 0:
        return 0
    if y > 0:
        if x > 0:
            return 1
        else:
            return 2
    else:
        if x < 0:
            return 3
        else:
            return 4


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
