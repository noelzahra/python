#while and for loops

#while loop
n = 0
# while statement stops when n = 5
while n < 5:
    print(n)
    n +=1
    
#for loops are faster than while loops
for letter in "Donught":
    print(letter)
    
#for loops in a range of numbers
for n in range(1, 10):
    print(n)
    
#nested for loops
for n in range(1, 4):
    for j in range(1, 4):
        print(f"n = {n} and j = {j}")
        
