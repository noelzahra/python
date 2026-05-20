#   lambda expressions as anonymous function. Can be passed as an argument
# 	Typically used for short, one-time operations
# 	Used with map(), filter(), and sorted() functions

import datetime as datetime


#anonymous function
add = lambda x, y: x + y
print(add (3, 4))

square = lambda x: x ** 2
print(square(5))

even_or_odd = lambda x: 'Even' if x % 2 == 0 else 'Odd' 
print(even_or_odd(9))

#lambda function in a list compehension
numbers = [1, 2, 3, 4, 5] 

squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

#lambda function with filter()
scores =[11, 12,14,17, 18, 20]

even_scores = list(filter(lambda x: x % 2 == 0, scores))
print(even_scores)

#lambda function with sorted()
students = [('Alice', 85), ('Bob', 90), ('Charlie', 80)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)


dates = ['2023-01-01', '2022-12-31', '2023-01-02']
sorted_dates = sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
formatted_dates = list(map(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').strftime('%d-%m-%Y'), sorted_dates))
print(formatted_dates)