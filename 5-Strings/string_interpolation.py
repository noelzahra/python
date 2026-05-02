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

#format string beofre Python 3.6, depracated now
print("{}kg is the weight of the {}".format(weight, animal))

print("{1}kg is the weight of the {0}.".format(animal, weight))

weight2 = 2.0
animal2 = "cat"
#format string after Python 3.6
print(f"{weight2}kg is the {animal2}\'s weight")
