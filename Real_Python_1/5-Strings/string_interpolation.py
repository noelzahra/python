from __future__ import print_function

# string interploation

numHeads = 1
numArms = 2
name = "Zoids"
print(name + " has " + str(numHeads) + " heads and " + str(numArms) + " arms.")

# Using .format()
print("========================\n" + "Using .fomrat() method")
print("{} has {} heads and {} arms.".format(name, numHeads, numArms))

# Assigning variable in .format()
print("{city} is a major {country} city with a population of\
 {population} million".format(city="New York", country="US", population=8.4))

# Exercises
print("=========================\n" + 'Exercises')

weight = 0.2
animal = "newt"
print(type(weight) is float)
print(type(animal) is str)
concat = str(weight) + "kg is the weight of the " + animal
print(concat)

print("{}kg is the weight of the {}".format(weight, animal))

print("{1}kg is the weight of the {0}.".format(animal, weight))

print("{}kg is the {}\'s weight".format(1, "cat"))
