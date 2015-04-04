from __future__ import print_function
from __future__ import division

prompt_base = raw_input("Enter base: ")
promt_exponent = raw_input('Enter exponent: ')
base = float(prompt_base)
exponent = float(promt_exponent)

output = base ** exponent
print("{} to the power of {} = {}".format(base, exponent, output))
