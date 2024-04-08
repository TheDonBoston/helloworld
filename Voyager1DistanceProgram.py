# Program to calculate various measurements of distance of Voyager 1
import datetime # imported in case calanders needed to be called upon

# Defining the given variables
distance_mi_tzero = 16637000000 # given in miles at the inital start date (t - 0), which I called "tzero"
velocity_mph = 38241 # given in miles/hour
miles_in_km  = 1.609344 # where km = kilometers
miles_in_au = 92955887.6 # where au = astronomical units
c = 299792458 # c is the speed of light, given in meters/second


# User input       
days_since = float(input("Enter the number of days since 09/25/2009: "))

# Calculating the miles, and converting miles to km and AU.
distance_mi = distance_mi_tzero + velocity_mph * 24 * days_since
distance_km = distance_mi * miles_in_km
distance_au = distance_mi / miles_in_au


radio_rt_comms = (2 * distance_mi) / c

# Multiple print functions will print the results line by line
print(f"Distance in miles from the Sun: {distance_mi}")
print(f"Distance in kilometers from the Sun: {distance_km}")
print(f"Distance in Astronomical Units: {distance_au}")
print(f"Round trip time for radio communication in hours: {radio_rt_comms}")