from __future__ import print_function

# lists are mutable arrays in python

color = ["red", "green", "blue", "yellow"]
scores = [2, 4, 6, 8]
mixed_list = ["car", 3, 4.0]

print(color[3])
print(scores)
print(mixed_list[1:3])

color[0] = "orange"
color[3] = "black"
print(color)

# append method
animals = []
animals.append("lion")
animals.append("tiger")
animals.append("zebra")
print(animals)

# remove method
animals.remove("lion")
animals.remove("tiger")
print(animals)

# extend method
cities = []
cities.append("New York")
cities.extend(["San Francisco", "Chicago", "Boston"])
print(cities)

# index
sports = ["running", "swiming", "cyclcing"]
print(sports.index("cyclcing"))

# copying one list into another
transport = ["car", "plane", "ship"]
all_transport = transport
all_transport.append("motorcycle")
print(transport)

# copying with extend()
sites = ["Niaggra falls", "Statue of Liberty", "Mount Rushmore"]
visit_sites = []
visit_sites.extend(sites)
print(visit_sites)

# sortign in alphabetical order
transport.sort()
print(transport)

# splitting a string
ingredients = "eggs, spam, po rocks, soya"
list = ingredients.split(",")
print(list)

print("==" * 8 + "\n\tlist methods\n" + "==" * 8)

desserts = ["ice cream", "cookies"]
desserts.sort()
print(desserts)
print(desserts.index("ice cream"))

# copy desserts into food
food = desserts[:]
print(food)

# Adding 2 items to food
food.append("broccoli")
food.append("turnips")
print(food, desserts)

# remove "cookies"
food.remove("cookies")
print(food)

# display the first two items
print(food[0:2])

# split a string
string = "cookies, cookies, cookies"
breakfast = string.split(", ")
print(breakfast)

print("==" * 8 + "\n\t\tExercises\n" + "==" * 8)


def list_numbers(array):
    for i in array:
        if(i >= 2) and (i <= 20):
            print(i)

output = list_numbers([2, 4, 8, 16, 32, 64])
print(output)

print("==" * 8 + "\n\t\tlist of lists\n" + "==" * 8)

cars = [
    ["Ford", 1900, 2014],
    ["Porsche", 2100, 2013],
    ["Renault", 1700, 2015],
    ["Audi", 2100, 2015],
    ["Mini", 1600, 2010]
]

for car in cars:
    print("Car brand: {}\nEngine: {}cc\nYear: {}\n==========".format(car[0],
          car[1], car[2]))
