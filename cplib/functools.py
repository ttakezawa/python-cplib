# Originated from
# - https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/bootstrap.py
# - https://pyrival.readthedocs.io/en/latest/bootstrap.html


def bootstrap(f, stack=[]):
    from types import GeneratorType

    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


def bootstrap_with_memo(f, stack=[], cache={}):
    from typing import Iterator

    def wrappedfunc(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if stack:
            stack.append(key)
            if key in cache:
                return iter([cache[key]])
            return f(*args, **kwargs)
        if key in cache:
            return cache[key]
        to = f(*args, **kwargs)
        while True:
            if isinstance(to, Iterator):
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                cache[stack.pop()] = to
                to = stack[-1].send(to)
        cache[key] = to
        return to

    return wrappedfunc
