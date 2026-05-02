#lambda expressions sma as anonymous function. Can be passed as an argument

#anonymous function
add = lambda x, y: x + y

print(add (3, 4))


value = lambda x: (x % 2 and "odd" or "even")(x)

print(value(9))