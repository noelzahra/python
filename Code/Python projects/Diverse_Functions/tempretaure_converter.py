#Converting between Fahrenheit and Celsius

def convert_to_fahrenheit(degrees_celsius):
    return float(degrees_celsius) * 9 / 5 + 32

def convert_to_celsius(degree_fahrenheit):
    degree_celsius = (float(degree_fahrenheit) - 32.0) * (5 / 9)
    return format(degree_celsius, ".3f")


print(f"100 C = {convert_to_fahrenheit(100)} F")
print(f"180 F = {convert_to_celsius(180)} C")
print(f"0 C = {convert_to_celsius(0)} F")
print(f"15 F = {convert_to_celsius(15)} C")

#unit_tests
assert convert_to_fahrenheit(0) == 32
assert convert_to_fahrenheit(100) == 212
#assert convert_to_celsius(convert_to_fahrenheit(15)) == 15
#assert convert_to_celsius(180) == 82.2222
#assert convert_to_celsius(0) == -17.778