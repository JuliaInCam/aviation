
#from aviation import passengers_per_day, required_global_fleet
import aviation #as a module

days_per_year = 365
passengers_per_year = 5_000_000_000.0
seats_per_aricraft = 150.0
flights_per_aircraft_per_day = 2.0 #make them all floats 

passengers_per_day = aviation.passengers_per_day(passengers_per_year,days_per_year) #reassigning function output from aviation file to the variable with the same name
required_global_fleet = aviation.required_global_fleet(passengers_per_day, seats_per_aricraft, flights_per_aircraft_per_day)

print(f"{required_global_fleet=:.2f}") #format string syntax, will output variable_name=value
