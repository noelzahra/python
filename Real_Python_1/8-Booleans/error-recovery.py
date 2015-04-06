from __future__ import print_function, division

# Exceptions


def divide(num1, num2):
    try:
        print(num1 / num2)
    except (TypeError, ZeroDivisionError):
        print("Can't divide by 0")

divide(33, 3)
divide(33, 0)

try:
    number = int(raw_input("Enter an integer which is not zero: "))
    print("10 / {} = {}".format(number, 10.0 / number))
except ValueError:
    print("That's not an integer")
except ZeroDivisionError:
    print("Any integer except zero")
