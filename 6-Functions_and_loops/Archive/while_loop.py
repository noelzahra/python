from __future__ import print_function

# 2 kinds  of loops in python for loop and while loops

# while loops
n = 1
while (n < 6):
    print("n = ", n)
    n += 1
print("loop done")


def while_loop(num1, num2):
    bananas = num1
    while (bananas < num2):
        print(bananas, "bananas")
        bananas += 1

shipping = while_loop(1, 8)
print(shipping)
