#Numbers and strings

num = '2'

print(num + num)
#Multiplies a string x 5
print(num * 5)

#Converting strings to int using int function

convert_to_integer = int(num)
print(convert_to_integer)
print(type(convert_to_integer))

array = ['1', '2', '4.01', '8.22']

for num in array:
     converted_num = float(num)
     print(converted_num, type(converted_num))
     
#Convert num into string with built-in str() function
num_pancakes = 10
print(type(num_pancakes))

total_eaten = "I ate " + str(num_pancakes) + " pancakes"
print(total_eaten)