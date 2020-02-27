import inspect
import typing


def type_check(func: typing.Callable):
    annotations = func.__annotations__
    arg_names = inspect.getargs(func.__code__)

    def out_func(*args):
        for arg in arg_names:
            ...
