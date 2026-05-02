
#setting to none, has class 'NoneType'
string = None
# print(type(string))

#Adding evens 
def adding_evens(num):
    sum_of_evens = 0
    string = None
    for n in range(2, num):
        if n % 2 == 0:
            sum_of_evens = sum_of_evens + n
            string = f"{n} = {sum_of_evens}"
            print(string)
        continue
       
# print(adding_evens(20))

#finding factors
def finding_factors(num):
    factors = []
    if num <= 0:
        print("Enter a number greater than zero")
    else:    
        for i in range(1, num):
            if num % i == 0:
                factors.append(i)
        return factors

print(finding_factors(0))
print(finding_factors(50))