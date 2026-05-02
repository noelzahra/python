from __future__ import division, print_function


def convert_to_fahrenheit(temp):
    convert_to_float = float(temp)
    celsius = (convert_to_float * 9 / 5) + 32
    return "{}F = {}C".format(temp, celsius)


def convert_to_celsius(temp):
    convert_to_float = float(temp)
    fahrenheit = (convert_to_float - 32) * (5 / 9)
    return "{}C = {}F".format(temp, fahrenheit)


print(convert_to_fahrenheit(37))
print(convert_to_celsius(90))
