"""Decorate fucntions as transforms."""

__all__ = ("Transform", "transform")

import collections.abc
import inspect
import typing


# the below is needed to enable for mypy to parse through @transform functions and make sure they are correct in any future code
class Transform[R, **P](typing.Protocol):  # not defining a class, just a type
    # 1 return type, then the parameters (any number)
    name: str
    parameters: tuple[str, ...]

    def __call__(*args: P.args, **kwargs: P.kwargs) -> R: ...


# higher order function - a function that operates on other functions:
def transform[
    R,
    **P,
](  # R is regular type variable, but **P is special type that has args and kwards attributes
    function: collections.abc.Callable[P, R],  # the function is a callable
) -> Transform[
    R, P
]:  # returns back a callable Transform c;lass that also has name and parameters attributes
    """Decorator to identify functions as tranforms."""
    transform = typing.cast("Transform[R, P]", function)
    transform.name = function.__name__  # setting the name which is the unique ID of this transform
    transform.parameters = tuple(
        inspect.signature(function).parameters.keys()  # parameters
    )  # will give me back the strings of parameter names of all of the parametes of my functionin a tuple
    return transform
