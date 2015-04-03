from __future__ import print_function

# More string exercises len function
string = "Allemagne"
stringLength = len(string)
print(stringLength)

stringA = "United"
stringB = "Kingdom"
concatString = stringA + stringB
thisStringLength = len(concatString)
print(thisStringLength)

stringC = "Great"
stringD = "Britain"
stringE = "Europe"
finalString = stringC, stringD, stringE
print("Great", "Britain", "Europe")

flavor = "Birthday cake"
findLetter = flavor[4]
print(findLetter)

# counts up to last number but doesn't include it
chars = flavor[0:5]
print(chars)

firstChars = flavor[:5]
print(firstChars)

lastChars = flavor[5:]
print(lastChars)

allChars = flavor[:]
print(allChars)

addChar = "F" + flavor[1:]
print(addChar)

addWord = flavor[:9] + "fun"
print(addWord)

# Exercises
newString = "Welcome"
newStringLength = len(newString)
print(newStringLength)

borough1 = "Manhattan"
borough2 = "Brooklyn"
borough3 = "Staten Island"
print(borough1, borough2, borough3)

phrase = "Python\'s frameworks include Django and Pyramid"
print(phrase)

multiLineString = """This string spans across
line1
line2
line3"""
print(multiLineString)

singleLineString = "String stays on one line\
eventhough it spreads on two lines"
print(singleLineString)

phrase = "bazinga"
subString = phrase[2:6]
print(subString)

# A more advanced way to do the above example would be:
start_index = 2
selection = phrase[start_index:len(phrase)-start_index+1]
print(selection)
