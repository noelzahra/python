# Function determinig if a number is odd or even

def isOdd(number):
    #Retrun whether a number modulus 2 is 1:
    return number%2 == 1

def isEven(number):
    #return whether a number modulus 2 is 0:
    return number%2 == 0

#testing
assert isOdd(42) == False
assert isOdd(99) == True
assert isOdd(-10) == False
assert isEven(42) == True
assert isEven(99) == False
assert isEven(-10) == True