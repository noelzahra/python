from __future__ import print_function

# Writing to files
my_output_file = open("hello.txt", "w")  # filename and 'w' for write
copy = "This is my first line\nPython is really easy to generate files\n\
Looking forward to start Django"
my_output_file.writelines(copy)

my_output_file = open("hello.txt", "a")   # appeding to exisiting file
next_paragraph = "\nPython has many other frameworks besides Django.\nThese \
include Pyramid, Flask and Tornado.\nSome libraries are really worth \
discovering"
my_output_file.writelines(next_paragraph)

my_output_file.close()  # always close file after initiating open
