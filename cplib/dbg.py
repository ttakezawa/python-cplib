import sys

if len(sys.argv) > 0 and sys.argv[0] == "./Main.py":

    def dbg(*objects: object) -> None:
        pass


else:

    import inspect
    import pathlib
    import pprint
    import sys

    def dbg(*objects: object) -> None:
        caller = inspect.stack()[1]
        path = pathlib.Path(caller.filename)
        at = f"{path.parent.name}/{path.name}:{caller.lineno}"
        repr = pprint.pformat(objects)
        print(f"{at} => \033[1;41m{repr}\033[0m", file=sys.stderr)
