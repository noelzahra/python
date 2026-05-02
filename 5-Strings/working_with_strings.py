from __future__ import print_function

# Strings fundmanetals

# Numbers as strings
number = "2"
print(number + number)

anotherNumber = "8"
print(anotherNumber * 5)

string = "12"
intFromString = int(string)
floatFromString = float(string)
caption = "This is a string converted to an int"
print("This is the original string:", string * 8)
print(caption, intFromString)
print('This is a string converted to a float', floatFromString)

newIntValue = intFromString * 4
newFloatValue = floatFromString * 3.3
print("Multiply:", newIntValue, newFloatValue)

# Converting int to a string
startInt = 22
convertToString = str(startInt)
print("String form an int:", convertToString)

# Data types: int, float and strings

print("=============" + '\n' + "Exercises" + '\n================')
# Exrecise
startString = "88"
print(type(startString))
convertToInt = int(startString)
print(type(convertToInt) is int, convertToInt * 10)

convertToFloat = float(startString)
print(type(convertToFloat) is float, convertToFloat * 0.5555)

firstString = "New York"
date = 1969
concat = firstString + " " + str(date)
print(type(concat) is str, concat)
