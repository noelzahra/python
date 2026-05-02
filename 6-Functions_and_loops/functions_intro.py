#Functions

#Built-in functions

variables = [3, 'age', 22.3, 0x2a]

for var in variables:
    print(f"{var} is {type(var)}")

print(type(print))
print(type(round))
print(type(max))
print(type(abs))

#Passing an arg in a built-in function
letters = len("pancake")
print(letters)

'''IMPORTNAT: Function executing:
    Function Call: args are passed to function
    Execution: Action is performed on args
    Return: Original function call is replaced with a return value
    Return is always at the end of the function
'''

#Function call, pass args
def greeting(first_name, second_name) -> str:
    #execution with args
    user_name = f"{first_name.capitalize()} {second_name.capitalize()}"
    #return string value
    return  f"Good morning {user_name}! \nToday is a good day to code some Python"

print(greeting("Noel", "Zahra"))