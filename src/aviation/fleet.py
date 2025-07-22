"""Modelling of the global fleet based on average passenger and aircraft data."""


def passengers_per_day(passengers_per_year, days_per_year):
    """The number of passegers per day globally.

    Args:
        passengers_per_year (float): The number of pasengers flying per year globally
        days_per_year (float): the number of days in the modelled year

    """
    return passengers_per_year / days_per_year


def required_global_fleet(
    passengers_per_day, seats_per_aircraft, flights_per_aircraft_per_day
):  # this function should take output of the prev funciton as a variable
    """The size of the required global fleet.

    Args:
        passengers_per_day (float): The number of passengers flying per day globally
        seats_per_aircraft (float): The average number of seats in a commercial aircraft
        flights_per_aircraft_per_day (float): The average number of flights a commercial aircraft
            makes a day

    """
    return passengers_per_day / (seats_per_aircraft * flights_per_aircraft_per_day)


# required_global_fleet(150.0, 2.0,)

# when defining function, use keyword arguments, otherwise they are positional arguments always have to be given the function in this order!!!
# keyword arguments: we assign the variable name to the argument so that the order doesnt matter
# def passengers_per_day(*, passengers_per_year, days_per_year = 365.0):  asterisk forces all arguments as keyword arguments, which will initiate keyword agruments for arguments placed after it in the input arguments
