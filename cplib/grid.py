from typing import List, TypeVar

T = TypeVar("T")


def rot_90(grid: List[List[T]]) -> List[List[T]]:
    return [list(reversed(v)) for v in zip(*grid)]
