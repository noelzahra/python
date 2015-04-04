from __future__ import print_function

# Find string from a string

# Find location os search term
phrase = "The surprise is in here somewhere"
search = phrase.find("surprise")
print(search)

notFound = phrase.find("New York")
print(notFound)
# When term is not found it returns -1

# find() only returns first string search term
firstStringOnly = "A string in a string".find("string")
print(firstStringOnly)

contactNumber = 447528911
print(str(contactNumber).find("7"))

# replace() method
header = "Python is a programming language that lets you work quickly\
 and integrate systems more effectively"
copy = header.replace("integrate systems", "build web applications")
print(copy + '\n' + header)

print("=========================\n" + 'Exercise')

print("AAA".find("a"))

update = "version 2.0"
v_num = 2.0
print(update.find(str(v_num)))

prompt = raw_input("What\'s your password")
print(prompt.find("a"))
