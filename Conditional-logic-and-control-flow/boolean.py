import math

#boolean comparator
''' > Greater thna
    < less than
    >= Greater than or equal
    <= Less than or equal
    != not equal to
    == equal to
'''

#True values
print(bool(10 > 5))
print(bool(1 < 2))
print(bool(10 >= 9))
print(bool(2 != '2'))
print(bool(2 == 2))

#false values
print(bool(8 > 10))
print(bool( 100 < 90))
print(bool("2" == 2))
print(bool(3 != 3))

'''logical operators
    & : both variables evalauate to TRUE
    or: One variable can evalaute to TRUE
    not: both varaibles evaluate to 
'''

#False
print(bool(2 >= 3))

#Not False = TRUE
output = (2 != 3) & (3 < 4)
output2 = (1 == '1') or (2 == 2)
output3 = not (40 > 50)
print (bool(output))
print(bool(output2))
print(bool(output3))


#Function with or
def check_if_prime(num):
    #define flag
    flag = False
    
    if num == 0 or num == 1:
        string = f"{num} is not a prime number"
    elif num > 1:
        #check for factors
        for i in range(2, num):
            if(num % i) == 0:
                #returning 0 from 
                flag = True
                #break out of loop
                break
    #check if flag is True
    if flag:
        string = f"{num}, is not prime but a composite number"
    else:
        string = f"{num}, is a prime number"
    return string

numbers = [1, 2, 3, 4, 5, 6, 7, 88, 97, 101 ]

for num in numbers:
    num_check = check_if_prime(num)
    print(num_check)
    
