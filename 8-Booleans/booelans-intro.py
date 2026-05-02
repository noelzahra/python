from __future__ import print_function, division

# Data-type: booleans
true_is_one = 42 + True
print(true_is_one)

false_is_zero = False * 2 - 3
print(false_is_zero)
print(type(false_is_zero))

val = True
print(type(val))

# Boolean comparators


def greater_than(num1, num2):
    print("{} > {}: {}".format(num1, num2, (num1 > num2)))

print("===================\ngreater than\t\t>\n===================")
greater_than(4, 2)
greater_than(2, 4)


def less_than(num1, num2):
    print("{} < {}: {}".format(num1, num2, (num1 < num2)))
print("===================\nless than\t\t<\n===================")
less_than(5, 8)
less_than(8, 5)


def greater_than_or_equal(num1, num2):
    print("{} >= {}: {}".format(num1, num2, (num1 >= num2)))
print("=========================\ngreater than or equal\t>=\n==============\
===========")
greater_than_or_equal(5, 5)
greater_than_or_equal(8, 5)
greater_than_or_equal(4, 9)


def less_than_or_equal(num1, num2):
    print("{} <= {}: {}".format(num1, num2, (num1 <= num2)))
print("===========================\nless than or equal\t\t>=\
 \n===========================")
less_than_or_equal(6, 6)
less_than_or_equal(6, 10)
less_than_or_equal(6, 3)


def is_not_equal(num1, num2):
    print("{} != {}: {}".format(num1, num2, (num1 != num2)))
print("======================\nnot equal\t\t!=\
 \n======================")
is_not_equal(4, 8)
is_not_equal(3, 3)


def is_equal(num1, num2):
    print("{} == {}: {}".format(num1, num2, (num1 == num2)))
print("======================\nis equal\t\t==\
 \n======================")
is_equal(4, 4)
is_equal(1, 3)

print("======================\n\t\tCompare strings\
 \n======================")

# string comparison


def compare_true_strings(str1, str2):
    if(str1 == str2):
        print("{} == {} is: {}".format(str1, str2, (str1 == str2)))
    else:
        print("{} != {} is: {}".format(str1, str2, (str1 == str2)))

compare_true_strings("dog", "dog")
compare_true_strings("cat", "dog")


def compare_false_strings(str1, str2):
    if(str1 != str2):
        print("{} != {}: {}".format(str1, str2, (str1 != str2)))
    else:
        print("{} != {}: {}".format(str1, str2, (str1 != str2)))

compare_false_strings("bird", "fish")
compare_false_strings("fish", "fish")

print("======================\n\t\tExercise\
 \n======================")

print(1 <= 1)
print(1 != 1)
print(1 != 2)
print("good" != "bad")
print("good" != "Good")
print(123 == "123")
