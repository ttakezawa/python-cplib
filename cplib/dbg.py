import inspect, pathlib, pprint, sys


def dbg(*objects: object) -> None:
    caller = inspect.stack()[1]
    path = pathlib.Path(caller.filename)
    at = f"{path.parent.name}/{path.name}:{caller.lineno}"
    repr = pprint.pformat(objects)
    print(f"{at} => \033[1;41m{repr}\033[0m", file=sys.stderr)
