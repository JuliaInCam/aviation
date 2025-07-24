"""Analysis to determine the number of passengers per day globally using models defined in `SRC/aviation`."""

import camia_engine as engine
from camia_model.units import year

import aviation
from aviation.units import passenger

passengers_per_year = 5_000_000_000.0 * passenger / year  # not a float anymore

inputs = {"passengers_per_year": passengers_per_year}
output = "passengers_per_day"

systems_model = engine.SystemsModel(aviation.transforms)  # equal to SystemModel Class
passengers_per_day = systems_model.evaluate(inputs, output)

print(f"{passengers_per_day=}")  # format string syntax, will output variable_name=value
