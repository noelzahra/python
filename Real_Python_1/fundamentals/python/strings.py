# strings
from __future__ import print_function

start = "A simple string"
start = start.upper()
print(start, type(start))

uppercaseString = "UPPERCASE STRING CONVERTED TO LOWERCASE"
lowercaseString = uppercaseString.lower()
print(uppercaseString + '\n' + lowercaseString)

initialString = "Python has numerous frameworks"
search = initialString.find("has")
print(search)

change = initialString.replace("has numerous", "has many popular")
print(change)

foundation = 1900
city = "new York"
concat = city.capitalize() + " was founded on: " + str(foundation)
print(concat)

'''
prompt = raw_input("Please enter your password")
check = prompt.find('A')
print(check)
'''

# Numbers and strings
print("==============\n" + "Numbers" + "\n==============")
year = "1999"
convert_to_int = int(year)
print(convert_to_int, type(convert_to_int))

pi = "3.142"
convert_to_float = float(pi)
print(convert_to_float, type(convert_to_float))

# String manipulation
print("==============\n" + "String manipulation" + "\n==============")
print("{}\'s destination is {} for the {} Aceleration course starting\
 this {}".format("Noel", "Seattle", "Python", "December"))
print("{2} years of experience in coding {1} with {3} and {0}\
 using {4}".format("Python", "web-apps", 5, "Javascript", "Django"))
