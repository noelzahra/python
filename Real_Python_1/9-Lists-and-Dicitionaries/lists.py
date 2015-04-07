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
