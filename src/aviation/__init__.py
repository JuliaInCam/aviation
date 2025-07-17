# this file makes python consider this directory as a module
# also manages the name space for the module

__all__ = ("passengers_per_day", "required_global_fleet")

from aviation.fleet import passengers_per_day, required_global_fleet
