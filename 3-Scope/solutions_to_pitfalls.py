'''Good dev practices:
    Use local names rather than global names
    Write self-contained funtions
    Try to use unique object names, irrespective of scope you're in
    Avoid global name modifications
'''

#global
counter = 0

def update_counter(current_counter):
    return current_counter + 1

counter = update_counter(counter)
print(counter)