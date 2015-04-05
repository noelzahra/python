from __future__ import print_function

# Break the flow of program used in conjunction with a for or while loop

for i in range(0, 4):
    if i == 2:
        break
    print(i)
print("finished with i = ", str(i))

'''
Continue jumps to the end of the loop but instead of ejiting it goes
back to the top of the loop and continues with the nejt item in the loop
'''

for j in range(0, 4):
    if j == 2:
        continue
    print(j)
print("finished with j = ", str(j))


def search_letter(phrase, char):
    for letter in phrase:
        if letter == char:
            print("Found \"{}\" in \"{}\"".format(char, phrase))
            break
    else:
        print("No letter \"{}\" in the \"{}\"".format(char, phrase))

search_letter("Getting really good at this", "x")
search_letter("Python is a great language to work with", "w")

# Exiting a while loop with a break
tries = 0
while tries < 3:
    password = raw_input("Password: ")
    if password == "pythoncoder":
        break
    else:
        tries += 1
else:
    print("Permission denied")
