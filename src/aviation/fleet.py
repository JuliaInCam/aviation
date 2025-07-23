"""Modelling of the global fleet based on average passenger and aircraft data. This is the source where actual formulas for models are defined as transforms."""

__all__ = ("passengers_per_day", "required_global_fleet")

import typing

import camia_model as model
from camia_model.units import Quantity, day, year

from aviation.units import aircraft, journey, passenger


@model.transform
# decorator does this passengers_per_day = transform (passengers_per_day)

def passengers_per_day(
    passengers_per_year: typing.Annotated[Quantity, passenger / year],
) -> typing.Annotated[Quantity, passenger / day]:
    # Any function name or argument is a unique indetifier within a modelling diagram.
    # Function has arrows flowing into it. Argument of a function has arrows flowing out of it.
    # These arent just function, we call them transfroms (because it adheres to the naming rules and
    # connect with leaf nodes and other tranforms)
    """The number of passengers per day globally.

    Args:
        passengers_per_year: The number of passengers flying per year globally
        days_per_year: the number of days in the modelled year

    """
    return passengers_per_year.convert_to(passenger / day)


@model.transform
def required_global_fleet(
    passengers_per_day: typing.Annotated[Quantity, passenger / day],
    seats_per_aircraft: typing.Annotated[Quantity, passenger / aircraft],
    flights_per_aircraft_per_day: typing.Annotated[Quantity, journey / (aircraft * day)],
) -> typing.Annotated[Quantity, aircraft]:
    # this function should take output of the prev funciton as a variable
    """The size of the required global fleet.

    Args:
        passengers_per_day: The number of passengers flying per day globally
        seats_per_aircraft: The average number of seats in a commercial aircraft
        flights_per_aircraft_per_day: The average number of flights a commercial aircraft
            makes a day
    """
    aircraft_per_journey = 1.0 * aircraft / journey
    return passengers_per_day / (
        seats_per_aircraft * flights_per_aircraft_per_day * aircraft_per_journey
    )


# when defining function, use keyword arguments, otherwise they are positional arguments always have to be given the function in this order!!!
# keyword arguments: we assign the variable name to the argument so that the order doesnt matter
# def passengers_per_day(*, passengers_per_year, days_per_year = 365.0):  asterisk forces all arguments as keyword arguments, which will initiate keyword agruments for arguments placed after it in the input arguments
