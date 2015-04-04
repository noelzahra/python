from __future__ import print_function
from __future__ import division

prompt_base = raw_input("Enter a base: ")
prompt_exponent = raw_input("Enter an exponent: ")

base = float(prompt_base)
exponent = float(prompt_exponent)
ouptut = base ** exponent
print("{} to the power of {} = {}".format(base, exponent, ouptut))
