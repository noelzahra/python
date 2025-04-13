#cube function
import math

def cube(num):
    return num ** 3

nums = [2, 3, 4, 5, 6, 7]
for num in nums:
    print(f"Cube of {num} is {cube(num)}")

#alternative cube solution
def exponent(num, power):
    return pow(num, power)

#dictionary with key value pairs as both int
results = {
    4 : 2,
    6 : 3,
    9 : 2,
    10: 2       
}

for value in results:
    print(f"{value} to the power of {results[value]} is {exponent(value, results[value])}")


#square root function
def root(num):
    value = float(math.sqrt(num))
    return f"{value:.2f}"

readings = [4.4, 8, 16, 80.5, 2020]

for value in readings:
    print(f"Root value of {value} is {root(value)}")