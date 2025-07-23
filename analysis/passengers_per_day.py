"""Analysis to determine the number of passengers per day globally using models defined in `SRC/aviation`."""

import aviation

days_per_year = 365
passengers_per_year = 5_000_000_000.0
seats_per_aricraft = 150.0
flights_per_aircraft_per_day = 2.0

passengers_per_day = aviation.passengers_per_day(passengers_per_year, days_per_year)

print(f"{passengers_per_day=:,}")  # format string syntax, will output variable_name=value
