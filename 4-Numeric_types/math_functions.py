#Math functions and Number methods
import math

pi = math.pi
shortened_pi = round(pi, 3)

print(shortened_pi)

#Rounding to the nearest even number when float ends with .5
floats = [2.3, 2.7, 2.5, 3.5, pi]
for float in floats:
    print(f"Rounding {float} to a whole integer {round(float)}")
    
#Absolute value: always gets the positive value
absolutes_list = [42, -42, 42.5, complex(3, 2)]
for absolute in absolutes_list:
    print(f"{absolute}, abs is {abs(absolute)}")

'''#Power function: pow(base, exp, mod=None)
pow1 = pow(5, 2)
pow2 = pow(2, -2)
pow3 = pow(2, 0.5)

#Passing modulus operator as a third arg
pow4 = pow(5, 2, 10)'''

power_list = [pow(5, 2), pow(2, -2), pow(2, 0.5), pow(5, 2, 10)]
for power in power_list:
    print(power)