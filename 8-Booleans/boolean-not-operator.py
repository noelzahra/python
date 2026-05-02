from __future__ import print_function

# Boolean not-operator
# when condition is NOT TRUE boolean is FALSE
# when condition is NOT FALSE boolean is TRUE


bool_one = not True   # must be False
bool_two = not False   # must nbe True
print(bool_one)
print(bool_two)


def bool_not(num1, num2):
    if(num1 < num2) and not (num1 == 1):
        return "{} < {} or {}".format(num1, num2, not False)
    else:
        return "{} < {} or {}".format(num1, num2, not True)

print(bool_not(4, 8))
print(bool_not(8, 4))

print("{} and not ({} != 1): {}".format(True, 1, (True and not(1 != 1))))
print("True and not (1 != 1) means True and True")

print("===================\n\t\tExercises\n===================")

print("(1 <= 1) and (1 != 1) bool is: {} and {} = {}\
      ".format((1 <= 1), (1 != 1), (1 <= 1) and (1 != 1)))
print("not (1 != 2) bool is: not {} = {}".format(not (1 != 2), (1 != 2),
                                                 not (1 != 2)))
print("(\"good\" != \"bad\") or False is: {} or {} bool is {}\
      ".format(("good" != "bad"), False, ("good" != "bad") or False))
print("(\"good\" != \"Good\") and not (1 == 1) is: {} and {} bool is: {}\
      ".format(("good" != "Good"), not (1 == 1), ("good" != "Good") and not
               (1 == 1)))
