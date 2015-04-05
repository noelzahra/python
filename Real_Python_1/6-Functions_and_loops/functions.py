from __future__ import print_function


def square(num):
    square_number = num ** 2
    return square_number

output = square(8)
print(output)


def add(num1, num2):
    total = num1 + num2
    return total
print(add(33, 11))


def subtractStd(num1, num2):
    if(num1 >= num2):
        return num1 - num2
    else:
        return num2 - num1

print(subtractStd(110, 300))
print(subtractStd(200, 90))

# Ternary operator
print("================\n" + "Ternary operator" + "\n================")


def subtract(num1, num2):
    """This is a ternary function which when TRUE returns num1 - num2,
       when FALSE returns else statment"""
    return num1 - num2 if num1 >= num2 else num2 - num1

help(subtract)
print(subtract(30, 20))
print(subtract(10, 50))


def division(num1, num2):
    return num1 / num2 if num1 >= num2 else num2 / num1

print(division(50, 5))
print(division(5, 40))


print("================\n" + "Exercise" + "\n================")


def cube(num):
    return num ** 3
print("4 cubed is:", cube(4))


def multiply(num1, num2):
    total = num1 * num2
    return "{} multiplied by {} = {}".format(num1, num2, total)

print(multiply(2, 5))
