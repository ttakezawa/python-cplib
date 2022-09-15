from typing import Any, List, Sequence as _Sequence


def ndarray(shape: _Sequence[int], default: Any = 0) -> List[Any]:
    if len(shape) == 1:
        return [default] * shape[0]
    return [ndarray(shape[1:], default) for _ in range(shape[0])]
