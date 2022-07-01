import sys

if len(sys.argv) > 0 and sys.argv[0] == "./Main.py":
    # then, it means AtCoder
    def dbg(*args: object) -> None:
        pass


else:
    import inspect
    import pathlib
    import re
    from pprint import pformat
    from typing import List

    def dbg(*args: object) -> None:
        caller = inspect.stack()[1]
        ctx = caller.code_context
        s = ctx[0] if ctx else ""
        path = pathlib.Path(caller.filename)
        at = f"{path.parent.name}/{path.name}:{caller.lineno}"
        matched = re.search(r"dbg\((.*)\)", s)
        names = []
        if matched:
            names = list(map(lambda x: x.strip(), matched[1].split(",")))
        if len(names) == len(args):
            vals: List[str] = []
            for name, arg in zip(names, args):
                if re.search(r"^'.+'|\".+\"$", name):
                    vals.append(str(arg))
                elif str(name) == str(arg):
                    vals.append(str(arg))
                else:
                    vals.append(f"{name}={pformat(arg)}")
        else:
            vals = [pformat(arg) for arg in args]
        cvals = [f"\033[1;41m{v}\033[0m" for v in vals]
        print(f"{at} => {', '.join(cvals)}", file=sys.stderr)
