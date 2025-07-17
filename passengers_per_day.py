import aviation

days_per_year = 365
passengers_per_year = 5_000_000_000.0
seats_per_aricraft = 150.0
flights_per_aircraft_per_day = 2.0 #make them all floats 

passengers_per_day = aviation. passengers_per_day(passengers_per_year, days_per_year)

print(f"{passengers_per_day=:.2f}") #format string syntax, will output variable_name=value
