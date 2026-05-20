# Find factors of a number

prompt = input("Enter a positive integer: ")
num = int(prompt)
for i in range(1, num + 1):
    if(num % i == 0):
        print("{} is a divisor of {}".format(i, num))
