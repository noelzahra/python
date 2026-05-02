# variable in global scope

# a variable is added to the global scope
num = 77

# print(globals())

'''LEGB rule:
    Local scope
    Enclsoing scope
    Gloabl scope
    Built-in scope
'''

#Local scope
#contians the names defined in a function
# Everytime you call a function, yu're also creating a new local scope

def create_username(first_name, second_name):
    #local scope has variable name
    name = f"{first_name.capitalize()} {second_name.capitalize()}"
    return name

print(create_username("pierre", "zahra"))

#GLobal scope
#top-most scope in Python program, script or module
#Only one global Python scope per program execution

#define the variable in diferent scopes
def print_total():
        #enclosing scope
        def inner_print_total():
            total = 7
            print(f"From inner function: {total=}")
            
    #outer scope but within larger func
        total = 12
        inner_print_total()
        print(f"From function: {total=}")
    
total = 5
print_total()
print(f"From global: {total=}")