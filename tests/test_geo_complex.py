import math
from typing import List
from unittest import TestCase

from cplib.geo_complex import Arg, arg_sort


class Test(TestCase):
    def test_arg_sort(self) -> None:
        points: List[complex] = [
            2 + 1j,
            1 + 8j,
            8 + 1j,
            2 + 3j,
            5 + 4j,
            0 + 0j,
            3 + -5j,
            3 + -4j,
            8 + -2j,
            4 + -3j,
            -1 + 2j,
            -1 + -2j,
            0 + 0j,
        ]
        points2 = points.copy()
        arg_sort(points)

        # rough sort
        points2.sort(key=lambda p: self.__class__._angle(p))

        assert points == points2

    def test_arg_object(self) -> None:
        points: List[complex] = [
            2 + 1j,
            1 + 8j,
            8 + 1j,
            2 + 3j,
            5 + 4j,
            0 + 0j,
            3 + -5j,
            3 + -4j,
            8 + -2j,
            4 + -3j,
            -1 + 2j,
            -1 + -2j,
            0 + 0j,
        ]
        # convert to Arg objects
        args = list(map(lambda p: Arg(p), points))
        args.sort()

        # rough sort
        points.sort(key=lambda p: self.__class__._angle(p))

        arg_points = list(map(lambda arg: arg.point, args))
        assert arg_points == points

    def test_arg_float(self) -> None:
        assert Arg(1.0 + 1.0j) == Arg(0.1 + 0.1j)
        assert Arg(1.0 + 0.0j) != Arg(0.0 + 1.0j)
        assert Arg(0.0 + 0.0j) == Arg(0 + 0j)

        assert Arg(0.1 + 0.5j) == Arg(0.000001 + 0.000005j)
        assert Arg(0.1 + 0.5j) <= Arg(0.000001 + 0.000005j)
        assert Arg(0.1 + 0.5j) >= Arg(0.000001 + 0.000005j)
        assert not (Arg(0.1 + 0.5j) < Arg(0.000001 + 0.000005j))
        assert not (Arg(0.1 + 0.5j) > Arg(0.000001 + 0.000005j))

        assert Arg(0.1 + 0.5j) == Arg(0.00000001 + 0.00000005j)
        assert Arg(0.1 + 0.5j) <= Arg(0.00000001 + 0.00000005j)
        assert Arg(0.1 + 0.5j) >= Arg(0.00000001 + 0.00000005j)
        assert not (Arg(0.1 + 0.5j) < Arg(0.00000001 + 0.00000005j))
        assert not (Arg(0.1 + 0.5j) > Arg(0.00000001 + 0.00000005j))

        almost_zero = math.sin(math.pi)

        # Because of the speficiation of math.isclose, we should take care of zero.
        # SEE: https://note.nkmk.me/python-math-isclose/
        assert not math.isclose(almost_zero, 0.0)
        assert math.isclose(almost_zero, 0.0, abs_tol=1e-15)

        assert Arg(almost_zero + 1j) == Arg(-almost_zero + 5j)
        assert Arg(almost_zero - almost_zero * 1j) == Arg(
            almost_zero + almost_zero * 1j
        )

    @staticmethod
    def _angle(p: complex) -> float:
        ang = Arg(p).degrees()
        if ang < 0:
            ang += 360
        return ang
