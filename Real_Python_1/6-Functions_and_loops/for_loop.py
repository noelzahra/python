from __future__ import print_function

print("=========================\n" + "Using for loop with a range" + "\n")
# for loops
for x in range(1, 8):
    print("x = ", x)
print("loop complete")


def for_loop(num1, num2):
    '''
    range ends before the last index
    '''
    for apples in range(num1, num2):
        print(apples, "apples")
cart = for_loop(3, 10)
print(cart)
help(for_loop)

print("\n=========================\n" + "Using for loop with a list")
# Using a list instead of range

for city in ["London", "Paris", "Stockholm", "Milan", "Barcelona", "Munich"]:
    print("Choose destination:", city)

for n in range(1, 4):
    for j in ["a", "b", "c"]:
        print("n =", n, "and j =", j)


print("\n=========================\n" + "Exercise")
# Exercise
print("\nfor loop")
for n in range(2, 11):
    print(n)

print("\nwhile loop")
y = 2
while(y < 11):
    print(y)
    y += 1


def doubles(num):
    return num * 2

base = 2
for i in range(0, 3):
    base = doubles(base)
    print(base)
