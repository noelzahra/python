from __future__ import print_function

# lists are mutable arrays in python

color = ["red", "green", "blue", "yellow"]
scores = [10, 8, 4, 6]
mixed_list = ["one", 2, 3.0]

print(color[2])
print(scores)
print(scores[1:3])

color[0] = "burgundy"
color[3] = "indigo"
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
cities.extend(["San Francisco", "Boston", "Chicago"])
print(cities)

# index
sports = ["running", "swimming", "cycling", "climbing"]
print(sports.index("cycling"))
