#Float type

list = [42, 3.168, 4.2e7, 0.726, 42_000_000.5]

for float in list:
    print(f"{float} is a {type(float)}")

#Exponents
exponents_list = [4.2e7, 5.8e-1]

for exp in exponents_list:
    print(f"{exp} approx: {format(exp, ".3f")}")
    
#Conversion to float
float('58')
float(66)
float("inf")
float("inf") > 50
float("nan")