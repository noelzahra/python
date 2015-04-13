from __future__ import print_function

my_input_file = open("hello.txt", "r")  # read file with "r"
# print(my_input_file.readlines()) '''will print line as a list'''
for line in my_input_file:
    print(line, end="")  # end ="" will output without a new \n
my_input_file.close()
