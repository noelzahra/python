from __future__ import print_function
from __future__ import division
# function


def square(num):
    square_num = num ** 2
    return square_num

input_num = 8
output_num = square(input_num)
print(output_num)


def subtract(num1, num2):
    if(num1 >= num2):
        return num1 - num2
    else:
        return num2 - num1

print(subtract(30, 10))
print(subtract(15, 50))


def subtract_ternary(num1, num2):
    return num1 - num2 if num1 >= num2 else num2 - num1
print(subtract_ternary(33, 99))


def division(num1, num2):
    return num1 / num2 if num1 >= num2 else num2 / num1

print(division(100, 10))
