from __future__ import print_function

my_input_file = open("hello.txt", "r")
line = my_input_file.readline()
while line != "":
    print(line, end="\n"),
    line = my_input_file.readline()

my_input_file.close()

# using a block
with open("hello.txt", "r") as my_input_file:
    for line in my_input_file.readlines():
        print(line, end=""),
my_input_file.close()
