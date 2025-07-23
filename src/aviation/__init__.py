# this file makes python consider this directory as a module
# also manages the name space for the module

"""A simple model of global aviation.

Modules:
   Fleet: Modelling of the global fleet based on average passenger and aircraft data.

"""

# only use triple quotes when you are writing a doc string

__all__ = (
    "passengers_per_day",
    "required_global_fleet",
    "transforms",
)  # adding these functions to the name space

from aviation.fleet import passengers_per_day, required_global_fleet

transforms = (
    passengers_per_day,
    required_global_fleet,
)  # tuple of transforms so it's easier to pass them all around together
