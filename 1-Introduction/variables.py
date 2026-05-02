#Variables

firstname = "Noel"
secondname = "Zahra"

firstname_secondname = firstname + " " + secondname
print (firstname_secondname)

firstnames = ["Noel", "Scott", "Pierre"]

for firstname in firstnames:
    print(f"User is {firstname} {secondname}")
    print(f"stored in {id(firstname)} and {id(secondname)}")
   
for firstname in firstnames:
    greeting = str(f"Welcome {firstname} {secondname}")
    print(f"{greeting} stored in {id(firstname)}")
    