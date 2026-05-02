#String methods BEGIN with a dot before method name
#Strings are immutable, variable holding string needs to be reassigned to change

#Converting to lowercase
phrase = "PYTHON CONVENTION"
phrase = phrase.lower()

print(phrase)

#Capitalize String method
capitalize_phrase = phrase.capitalize()
print(capitalize_phrase)


#Uppercase String Method
uppercase_phrase = phrase.upper()
print(uppercase_phrase)

#functions do not start with a dot
len(phrase)

#removing whitespace
new_phrase = "       Let's do coding"
remove_whitespace = new_phrase.lstrip()
print(remove_whitespace)

other_phrase = "Python to the win   "
remove_end_whiotespace = other_phrase.rstrip()
print(remove_end_whiotespace)

phrases = [new_phrase, other_phrase]
for phrase in phrases:
    phrase.strip()
    print(phrase)
    
#Bool
bool = new_phrase.startswith('Le')
print(bool)
bool2 = other_phrase.startswith('Py')
print(bool2)

bool3 = phrase.islower()
print(phrase)
print(bool3)