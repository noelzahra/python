my_input_file = open("new-textfile.txt", "w")  # write text to a file
copy = "This is a new text file to test skills gained in creating text files.\n\
This textfile tests more functionality with python and its frameworks.\n\
Besides the fundamentals in functional programming we need to cover OOP.\n"
my_input_file.writelines(copy)

my_input_file = open("new-textfile.txt", "a")  # append text to a file
new_text = "Further functionality can be gained form python libraries.\n\
The most used libraries include numpy, pandas and scipy.\n\
Most known frameworks include pyramid, Django and flask."
my_input_file.writelines(new_text)

my_input_file.close()