from __future__ import print_function


def invest(amount, rate, time):
    print("prinicpal amount: ${}".format(amount))
    print("annual rate of return: {}".format(rate))
    for i in range(1, (time + 1)):
        amount = amount * (1 + rate)
        print("year {}: ${}".format(i, amount))
    print("========================\n")

invest(100, 0.05, 8)
invest(2000, 0.025, 5)
