cars = 100 # Number of cars
space_in_a_car = 4 # Number of people in a car
drivers = 30 # Number of drivers
passengers = 90 # Number of passengers
cars_not_driven = cars - drivers # Number of cars that are not driven
cars_driven = drivers # Cars driven or used
carpool_capacity = cars_driven*space_in_a_car
average_passengers_per_car = passengers/cars_driven

print "There are ", cars, "cars available."
print "There are only ", drivers, "drivers available."
print "There will be ", cars_not_driven, "empty cars today."
print "We can transport ", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
