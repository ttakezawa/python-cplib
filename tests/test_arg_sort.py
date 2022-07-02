from math import atan2, pi
from typing import List
from unittest import TestCase

from cplib.arg_sort import Point, arg_sort


class Test(TestCase):
    def test_arg_sort(self) -> None:
        points: List[Point] = [
            (2, 1),
            (1, 8),
            (8, 1),
            (2, 3),
            (5, 4),
            (0, 0),
            (3, -5),
            (3, -4),
            (8, -2),
            (4, -3),
            (-1, 2),
            (-1, -2),
            (0, 0),
        ]
        points2 = points.copy()
        arg_sort(points)

        # rough sort
        points2.sort(key=lambda p: self.__class__._angle(p))

        assert points == points2

    @staticmethod
    def _angle(p: Point) -> float:
        x, y = p[0], p[1]
        rad = atan2(y, x)
        ang = rad * 180 / pi
        if ang < 0:
            ang += 360
        return ang
