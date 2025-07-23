"""Analysis to determine the number of passengers per day globally using models defined in `SRC/aviation`."""

# from camia import _engine as engine
import camia_engine as engine

import aviation

days_per_year = 365.25
passengers_per_year = 5_000_000_000.0


inputs = {  # dictionary with strings as keys and floats as values
    "passengers_per_year": passengers_per_year,
    "days_per_year": days_per_year,
}

output = "passengers_per_day"

systems_model = engine.SystemsModel(aviation.transforms)  # equal to SystemModel Class
passengers_per_day = systems_model.evaluate(inputs, output)

print(f"{passengers_per_day:.0f}")  # format string syntax, will output variable_name=value
