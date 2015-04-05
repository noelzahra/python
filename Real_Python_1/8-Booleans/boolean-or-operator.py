from __future__ import print_function

# Boolean or-operator
# At least one condition or both should be true


def bool_or(num1, num2, num3, num4):
    if(num1 < num2) or (num3 < num4):
        return "{} < {} or {} < {}: {}".format(num1, num2, num3, num4,
                                               (num1 < num2) or(num3 < num4))
    else:
        return "{} < {} or {} < {}: {}".format(num1, num2, num3, num4,
                                               (num1 < num2) or(num3 < num4))

print("Both are true:\n", bool_or(2, 4, 6, 8))
print("Both are false:\n", bool_or(4, 2, 8, 6))
print("First statement is true:\n", bool_or(4, 8, 6, 3))
print("Second statement is true:\n", bool_or(6, 3, 4, 8))

both_true = True or True
first_false = False or True
second_false = True or False
all_false = False or False
print("True or True:", both_true)
print("False or True:", first_false)
print("False or True:", second_false)
print("False or False:", all_false)

# You can combine or and operators together


def performance(num1, num2, num3, num4):
    if((num1 < num2) or ((num3 < num4) and (num2 < num4))):
        return "{} < {} or {} < {} and {} <{}: {}\
        ".format(num1, num2, num3, num4, num2, num4, (num1 < num2) or
                 ((num3 < num4) and (num2 < num4)))
    else:
        return "{} < {} or {} < {} and {} <{}: {}\
        ".format(num1, num2, num3, num4, num2, num4, (num1 < num2) or
                 ((num3 < num4) and (num2 < num4)))

print(performance(10, 20, 30, 40))
print(performance(40, 10, 20, 30))
print(performance(10, 40, 30, 20))
print(performance(40, 10, 30, 20))
