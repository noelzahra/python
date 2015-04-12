from __future__ import print_function

print("===================\n\t\tList\n===================")
# a list is a mutable array
colors = ["green", " blue", "orange"]
years = [2007, 1999, 1969]
mixed_list = [years[1], colors[2]]

print(colors[0])
print(years[1])
print(mixed_list)

# append
animals = []
animals.append("cat")
animals.append("dog")
animals.append("bird")
print(animals)

# remove and pop(i)
animals.remove("bird")
animals.remove("dog")
animals.append("fish")
animals.append("horse")
print(animals)
animals.pop(2)
print(animals)

# extend
cities = []
cities.extend(["New York", "San Francsisco", "Chicago"])
print(cities)
cities.append("Boston")
print(cities)
cities.pop(2)
print(cities)

# index
locations = ["London", "Milan", "Munich", "Zurich"]
desired_location = locations.index("Munich")
print(locations[2] + " is at index: " + str(desired_location))

# sort
locations.sort()
print(locations)

# split
ingredients = "eggs, bacon, crepe, coffee"
ingredients.split(",")
print(ingredients)


def list_numbers(array):
    for i in array:
        if(i >= 2) and (i <= 32):
            print(i)
output = list_numbers([2, 4, 8, 16, 32, 64, 128])

# list in lists
forests = [
            ["Italy", "Gran Paradiso", 1899],
            ["England", "Snowdonia", 1909],
            ["Germany", "Black Forest", 1880],
            ["France", "Pyrennes", 1790]
]

for forest in forests:
    print("Country: {} protected forest: {} in {}".format(forest[0],
                                                          forest[1],
                                                          forest[2]))

print("\n===================\n\t\tTuples\n===================")
# a tuple is an immutabe array

sports = ("running", "swimming", "cycling")
print(sports, type(sports))

cardinal_nums = ("first", "second", "third")
print(cardinal_nums)
print(cardinal_nums[2])
pos1, pos2, pos3 = cardinal_nums
print(pos1)
print(pos2)
print(pos3)

# a dictionary with key-value pairs
print("\n===================\n\t\tDictionary\n===================")
phonebook = {
              "Pierre": 79796040,
              "Home": 21693626,
              "Ruth": 79458001,
              "Noel": 79798002
}

print(phonebook)
print(phonebook["Noel"])
