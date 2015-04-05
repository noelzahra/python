from __future__ import print_function, division

start = 'Simple string to uppercase'
start = start.upper()
print(start)

lowerString = "LOWERCASE STRING"
print(lowerString.lower())

anotherString = "small leters"
print(anotherString.capitalize())

initialString = 'Python has many frameworks including Django'
searchTerm = initialString.find("Django")
print(searchTerm)

change = initialString.replace(" has many", "\'s many popular")
print(change, "Length: {}".format(len(change)))

phrase = "bazinga"
print(phrase[2:6])

anotherPhrase = "Singularity"
start_index = 6
selection = anotherPhrase[start_index:len(anotherPhrase)]
print(selection)

'''
prompt = raw_input("What's on your mind right now? ")
print("You said: ", prompt)

string = raw_input("Which year? ")
year = int(string)
city = raw_input("Which city? ")
output = "{} is the most popular city in {}".format(city, year)
print(output)
'''

print("======================\n\t\t\tData types\n======================")

strings = ["79798002", "3.142", 1969]
contact = int(strings[0])
pi_const = float(strings[1])
dob = str(strings[2])
print("Contact number: {}\nPreferred constant: {}\nDate of birth: {}"
      .format(contact, pi_const, dob))
print("Contact is an: {}\nConstant is a: {}\nDate is a str: {}"
      .format(type(contact), type(pi_const), type(dob) is str))

print("======================\n\t\t\tFunctions\n======================")


def sum(num1, num2):
    return num1 + num2


def multiply(num1, num2):
    return num1 * num2


def subtract(num1, num2):
    return num1 - num2 if(num1 >= num2) else num2 - num1


def divide(num1, num2):
    return num1 / num2 if(num1 >= num2) else num2 / num1

print("Sum: ", sum(25, 50), "\nMultipy: ", multiply(100, 2), "\nsubtract: ",
      subtract(90, 120), "\nDivision: ", divide(2, 50))


def square(num):
    return num ** 2
print(square(4))


def cubed(num):
    return num ** 3
print(cubed(3))


def convert_to_celsius(temp):
    celsius = (float(temp) * 9 / 5) + 32
    return "{}degF = {}degC".format(temp, celsius)
print(convert_to_celsius(30))

print("======================\n\t\t\tLoops\n======================")


def while_loop(num):
    n = num
    while (n < 12):
        print("n =", n)
        n += 1
    print("loop done")
loop = while_loop(8)


def for_loop(num1, num2):
    for apples in range(num1, num2):
        print(apples, "apples")
cart = for_loop(2, 6)


def invest(amount, rate, years):
    print("Initial capital: ${}".format(amount))
    print("Rate of return: {}%".format(rate))
    for i in range(1, years):
        amount = amount * (1 + rate)
        print("Year{}: ${}".format(i, amount))

    print("Your investment has matured")

invest(100, 0.05, 10)
