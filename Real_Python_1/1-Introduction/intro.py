import datetime

date = datetime.date(1969, 12, 21)
name4 = 'Noel'
dob = 'Birthday'

print(f"{name4}'s {dob} is on {date}")

# # Basic print command
print("Hello World")

name = "Pierre"
print(name)

concat = "============" + "\n" + name + " " + "Zahra" + "\n" + "============"
print(concat)

# # Maths
sum = 2 + 2
print(sum)

# # Python 3
print('Python 3 print function')

# # strings
phrase = "Scott"
location = "Valletta"
message = "Welcome" + " " + phrase + " from " + location
print(message)

# '''
# This is a long comment that can be split one more than one line
# '''
sports = "running" + "\n" + "is #1 sport"
string_number = "\n" + "1234"
print(sports, string_number)

subString = """This is a substring in a string: 'Python is awesome' since it
makes it possible to code in a few lines"""
print(subString)

anotherSubstring = "This is another substring 'Python is easy to master'"
print(anotherSubstring)

punctuation = "Python\'s frameworks include Django, Flask and Pyramid"
print(punctuation)

multiString = """This string spans on multiple lines
First line
Second line
Last line"""
print(multiString)

longString = "This is a long string which is uninterrupted \
and should continue on the same line with the addition of a backslash"
print(longString)
#type of variable
print(type(longString))
