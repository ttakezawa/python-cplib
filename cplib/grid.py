from typing import List, TypeVar as _TypeVar

_T = _TypeVar("_T")


def rot_90(grid: List[List[_T]]) -> List[List[_T]]:
    return [list(reversed(v)) for v in zip(*grid)]
