#print integer

for i in range(2, 11):
    print(i)
    
#doubles function

def doubles(num):
    double = num * 2
    return double

n = 2
#For loop with _ , wher eunderscore is a throaway value not used in loop
for _ in range(3):
    n = doubles(n)
    print(n)