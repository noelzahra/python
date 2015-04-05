from __future__ import print_function

# Control flow


def flow():
    if(True):   # if condition is True
        return "Execute command"


def check_total(num1, num2):
    if((num1 + num2) == num1 * 2):
        print("{} + {} == {} * 2: {}".format(num1, num2, num1, (num1 * 2)))

check_total(4, 4)


def destination(country, city):
    if ((country == "UK") and (city == "London")):
        print("Currency is {} for {}".format("GBP", city))
    else:
        print("Currency is {} for {}".format("Euro", "Europe"))

destination("UK", "London")
destination("Munich", "Germany")


def another_destination(country, city):
    if ((country == "UK") or (city == "London")):
        print("Currency is {} for {}".format("GBP", country))
    elif ((country == "Germany") or (city == "Munich")):
        print("Currency is {} for {}".format("Euro", country))
    elif ((country == "France") or (city == "Paris")):
        print("Currency is {} for {}".format("Euro", country))
    elif ((country == "Italy") or (city == "Rome")):
        print("Currency is {} for {}".format("Euro", country))
    elif ((country == "Spain") or (city == "Madrid")):
        print("Currency is {} for {}".format("Euro", country))
    else:
        print("Currency is {} for {}".format("$", country))

another_destination("France", "Paris")
another_destination("Italy", "Milan")
another_destination("UK", "Manchester")
another_destination("US", "Seattle")

# Always start with IF you can do an if/elif an if/else and an if/elif/else
# If you want to test 2 seperate conditions do 2 different IF statements


def sport_selection(age, weight):
    if ((age > 14) and (age <= 30)):
        if ((weight < 80) and (weight > 55)):
            print("Age: {}years and weight: {}kg: Sports clasification: {}\
                  ".format(age, weight, "Cycling"))
        elif((weight > 80)):
            print("Age: {}years and weight: {}kg: Sports clasification: {}\
                  ".format(age, weight, "Weightlifting"))
        elif((weight < 55)):
            print ("Age: {}years and weight: {}kg: Sports clasification: {}\
                  ".format(age, weight, "Gymnastics"))
    elif((age > 30) and (age < 50)):
        print("Age: {}years and weight: {}kg: Sports clasification: {}\
                  ".format(age, weight, "Running"))
    elif((age > 50)):
        print("Age: {}years and weight: {}kg: Sports clasification: {}\
                  ".format(age, weight, "Swimming"))
    else:
        print("Age: {}years and weight: {}kg: Sports clasification: {}\
                  ".format(age, weight, "No suitable sports available"))

sport_selection(22, 40)
sport_selection(13, 40)
sport_selection(30, 60)
sport_selection(55, 60)

print("===================\n\t\tExercises\n===================")

prompt = raw_input("Password: ")
if (len(prompt) > 5):
    print("{} is too long".format(prompt))
elif(len(prompt) < 5):
    print("{} is too short".format(prompt))
else:
    print("Password accepted: {}".format(prompt))
