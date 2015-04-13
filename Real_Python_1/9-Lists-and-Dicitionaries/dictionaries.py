from __future__ import print_function

# a dicitionary stores a collection of objects
# dictionaries store data in pairs as a key-value pair
# lists use []
# tuples us ()
# dicts use {}
# key/value pairs in dicts are stored as hashes = we don;t care about the
# index but the which value belongs to which key

phonebook = {
            "Pierre": 7976940,
            "Noel": 79798002,
            "Ruth": 79458001,
            "Home": 721683626
}

print(phonebook)
print(phonebook["Pierre"])  # access value by key instead of an index

# adding new entries
phonebook["Uniblue"] = "23275000"
print(phonebook)

# getting all the keys
print(phonebook.keys())

# deleting an entry
del(phonebook["Home"])
print(phonebook)

# looping through a dictionary
for name in phonebook:
    print(name, phonebook[name])

# Bool key in dictioanry
check = "Noel" in phonebook
print(check, type(check))
check_more = "Sydney" in phonebook
print(check_more, type(check_more))

# access dict in sorted order - sorting function is temporarily
paragliders = {
                "Buzz": 13,
                "Mantra": 20,
                "Viper": 18,
                "Rush": 16
}

for glider in sorted(paragliders):
    print(glider, paragliders[glider])

# dictionaries holding other dictionaries
contacts = {
            "Noel": {"cell": 79798002, "work": 23275000},
            "Pierre": {"cell": 79796040, "work": 23275000},
            "Drew": {"cell": 79778080, "work": 332891033}
}

print(contacts)
print(contacts["Noel"])
print(contacts["Pierre"]["cell"])


# dict() using string keys without quotes (zone1, zone2, zone3)
first_dict = dict(zone1="London", zone2=4101, zone3=88990)
print(first_dict)

# dict to store tuples
fibs_dict = dict(
                   [("fib1", 0.268), ("fib2", 0.382), ("fib3", 0.618)]
                   )
print(fibs_dict)

print("\n===================\n\t\tExercises\n===================")
# Birthday list

birthdays = {
            "Pierre": {"month": "March", "day": 30, "year": 1999},
            "Scott": {"month": "December", "day": 15, "year": 2007},
            "Noel": {"month": "December", "day": 21, "year": 1969}
}

print(birthdays["Noel"])

star_wars_birthdays = {}
star_wars_birthdays["Luke Skywalker"] = {"month": "May", "day": 24,
                                         "year": 1965}
star_wars_birthdays["Obi-Wan Kenobi"] = {"month": "March", "day": 11,
                                         "year": 1957}
star_wars_birthdays["Darth Vader"] = {"month": "April", "day": 1,
                                      "year": 1941}
print(star_wars_birthdays)


def check_name(dictionary):
    for name in ["Yoda", "Darth Vader"]:
        if name not in dictionary:
            dictionary[name] = "unknown"
    print("Yoda: {}\nDarth Vader: {}".format(dictionary[name],
                                             dictionary[name]))

check_name(star_wars_birthdays)

print("\n===================\n\t\tloop keys\n===================")
for name in star_wars_birthdays:
    print(name, star_wars_birthdays[name])

del(star_wars_birthdays["Darth Vader"])
print(star_wars_birthdays)

birthdays_dict = dict(
                      [("Luke Skywalker", "5/15/19"),
                       ("Obi-Wan-Kenobi", "3/11/57"),
                       ("Darth Vader", "4/1/41")]
                      )
print(birthdays_dict)
