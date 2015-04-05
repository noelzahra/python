from __future__ import print_function

# and logical operator
# Both conditionals should be true


def bool_and(num1, num2, num3, num4):
    if(num1 < num2) and (num3 < num4):
        return "{} < {} and {} < {}: {}".format(num1, num2, num3, num4, (num1 <
                                                num2) and (num3 < num4))
    else:
        return "{} < {} and {} < {}: {}".format(num1, num2, num3, num4, (num1 <
                                                num2) and (num3 < num4))

print("Both are true:\n", (bool_and(2, 3, 6, 8)))
print("First statement is false:\n", bool_and(3, 2, 6, 8))
print("Second statement is false:\n", bool_and(2, 3, 8, 6))
print("Both statements are false:\n", bool_and(5, 2, 8, 4))

both_true = True and True
first_false = False and True
second_false = True and False
all_false = False and False
print("True and True:", both_true)
print("False and True:", first_false)
print("False and True:", second_false)
print("False and True:", all_false)
