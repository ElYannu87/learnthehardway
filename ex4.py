# number of total cars
cars = 100
# total space for people in one car
space_in_a_car = 4
# total number of drivers
drivers = 30
# total number of passengers
passengers = 90
# substraction of the number of cars minus the number of drivers
cars_not_driven = cars - drivers
# number of cars in action is equal to the number of drivers
cars_driven = drivers
# total capacity of the cars : cars multiply space
carpool_capactity = cars_driven * space_in_a_car
# average number of people in one car
average_passenger_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capactity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passenger_per_car, "in each car.")
