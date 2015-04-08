from __future__ import print_function

# tuples are immutable arrays

tuple_one = ["a", "tuple", "cannot", "be", "changed"]
print(tuple_one)

# no methods like append() or sort()
# index() method is available

print(tuple_one[2])

# When a function returns multiple values it's best to storwe them in a tuple


def adder_subtractor(num1, num2):
        add = (num1 + num2)
        subtract = (num1 - num2)
        return (add, subtract)  # returns a tuple (brackets are optional)

print(adder_subtractor(4, 1))
output = adder_subtractor(6, 3)
print("Function returns: {}\nAddition result: {}\nSubtraction result: {}\
 \nType is {}".format(output, output[0], output[1], type(output)))


def find_coordinates(lat, longt):
    lat = lat
    longt = longt
    return (lat, longt)   # tuple packing

map_coordinates = find_coordinates(4.21, 9.29)
print("Latitude: {}\nLangitutde: {}".format(map_coordinates[0], map_coordinates
      [1]))

sports = ("running", "swimming", "cycling")
x, y, z = sports    # tuple unpacking
print(x)
print(y)
print(z)

print("==" * 8 + "\n\t\tExercise\n" + "==" * 8)

cardinal_nums = ("first", "second", "third")

# Display the second object in the tuple
print(cardinal_nums[1])

# unpack the tuple into three strings and display them
pos1, pos2, pos3 = cardinal_nums
print(pos1)
print(pos2)
print(pos3)
