import math
import sys
from typing import List
from unittest import TestCase

from cplib.arg_sort import Arg, Point, arg_sort


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

    def test_arg_object(self) -> None:
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
        # convert to Arg objects
        args = list(map(lambda p: Arg(p[0], p[1]), points))
        args.sort()

        # rough sort
        points.sort(key=lambda p: self.__class__._angle(p))

        arg_points = list(map(lambda arg: (arg.x, arg.y), args))
        assert arg_points == points

    def test_arg_float(self) -> None:
        assert Arg(1.0, 1.0) == Arg(0.1, 0.1)
        assert Arg(1.0, 0.0) != Arg(0.0, 1.0)
        assert Arg(0.0, 0.0) == Arg(0, 0)

        assert Arg(0.1, 0.5) == Arg(0.000001, 0.000005)
        assert Arg(0.1, 0.5) <= Arg(0.000001, 0.000005)
        assert Arg(0.1, 0.5) >= Arg(0.000001, 0.000005)
        assert not (Arg(0.1, 0.5) < Arg(0.000001, 0.000005))
        assert not (Arg(0.1, 0.5) > Arg(0.000001, 0.000005))

        assert Arg(0.1, 0.5) == Arg(0.00000001, 0.00000005)
        assert Arg(0.1, 0.5) <= Arg(0.00000001, 0.00000005)
        assert Arg(0.1, 0.5) >= Arg(0.00000001, 0.00000005)
        assert not (Arg(0.1, 0.5) < Arg(0.00000001, 0.00000005))
        assert not (Arg(0.1, 0.5) > Arg(0.00000001, 0.00000005))

        almost_zero = math.sin(math.pi)

        # Because of the speficiation of math.isclose, we should take care of zero.
        # SEE: https://note.nkmk.me/python-math-isclose/
        assert not math.isclose(almost_zero, 0.0)
        assert math.isclose(almost_zero, 0.0, abs_tol=1e-15)

        assert Arg(almost_zero, 1) == Arg(-almost_zero, 5)
        assert Arg(almost_zero, -almost_zero) == Arg(almost_zero, almost_zero)

    @staticmethod
    def _angle(p: Point) -> float:
        x, y = p[0], p[1]
        rad = math.atan2(y, x)
        ang = rad * 180 / math.pi
        if ang < 0:
            ang += 360
        return ang
