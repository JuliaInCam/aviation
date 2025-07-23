"""Analysis to determine the required size of the global fleet using transforms defined in `src/aviation`."""

import camia_engine as engine

import aviation

days_per_year = 365.0
passengers_per_year = 5_000_000_000.0
seats_per_aircraft = 200.0
flights_per_aircraft_per_day = 2.0  # make them all floats


inputs = {  # dictionary with strings as keys and floats as values
    "passengers_per_year": passengers_per_year,
    "days_per_year": days_per_year,
    "seats_per_aircraft": seats_per_aircraft,
    "flights_per_aircraft_per_day": flights_per_aircraft_per_day,
}

output = "required_global_fleet"

systems_model = engine.SystemsModel(aviation.transforms)  # equal to SystemModel Class
required_global_fleet = systems_model.evaluate(inputs, output)

print(f"{required_global_fleet:.0f}")  # format string syntax, will output variable_name=value
