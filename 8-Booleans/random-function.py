from __future__ import print_function
from random import randint

print(randint(0, 1))   # 50/50 chance of 0 or 1

# heads otr tails
heads = 0
tails = 0

for trial in range(0, 1000):
    while randint(0, 1) == 0:
        tails += 1
    heads += 1
print("heads / tails = {}".format(heads / tails))
