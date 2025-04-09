'''from __future__ import print_function
from __future__ import division
'''
# Maths
add_total = 6 * (1 + 6)
print(add_total)

print("=========================\n" + "Arithmetic operators")


'''Arithmetic operators
   There are seven arithmetic operators in Python
   They are binary as they take two operands
'''
#Addiiton
def addition(int1, int2):
    return int1 + int2

sum = addition(3, 5)
print(sum)

def subtraction(int1, int2):
    if (int1>int2):
        return int1 - int2
    else:
        return int2 - int1
    
subtract = subtraction(33, float(66.4))
print(subtract)

def multiplication(int1, int2):
    return int1 * int2

multiply = multiplication(2.5, 10)
print(multiply)

def exponentiation (num1, num2):
    return num1 ** num2

exponent = exponentiation(2.5, 5)
print(exponent)

#standard division
def division(num1, num2):
    return num1 / num2

print(division(200,33))

#Floor division: division to the nearest whole int
def floor_division(num1, num2):
    return num1 // num2

print(floor_division(200, 33))

#Modulus, calculates the remainder
def modulus(num1, num2):
    return num1 % num2

modulus_output = modulus(5, 2)
'''2 * 2 = 4, remains 1'''
print(modulus_output)

'''python can only add dnumbers of compatible data types
    When an int and a float are added, Python considers
    the variables as both float
'''
print(multiplication(22, 1.5))

#integer literal
output1 = int(3/2)
output2 = int(-3/2)
output3 = int(-3/2)
#floor division rounds up to the nearest whole int
output_floor = int(-3//2)

list = [output1, output2, output3, output_floor]

for output in list:
    print(output)
    
#Operator **
power_of_3 = 5 ** 3
exponent3 = 5 ** -3
square_root = 2 ** 0.5

math_list = [power_of_3, exponent3, square_root]

for math in math_list:
    print(math)
    
#Modulus operator
modulus1 = 5 % 3
modulus2 = 20 % 7
modulus3 = 16 % 8

modulus_list = [modulus1, modulus2, modulus3]
for modulus in modulus_list:
    if (modulus == 0):
        print(f"Is even because modulus is {modulus}")
    else:
        print(modulus)
        
#Using operators together
'''Operator Precedence: topmost get executed first
    ()
    **
    +x, -x
    *, /, //, %
    +, -
'''
total = 2 + 3 * 1.5
brackets_first = (2 + 3) * 1.5
print(f"Muliplication first: {total}, Brackets first: {brackets_first}")

#floating point representation error
float_error = 0.1 + 0.2
print(float_error)