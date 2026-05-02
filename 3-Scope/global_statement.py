#global statement

counter = 0

def update_counter():
    counter +=1

# update_counter()

#Traceback: UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value

#For this to work. first assign the global counter into the function local scope

def run_counter():
    global counter
    #tell function to work with the global variable counter
    counter +=1
    print(counter)

run_counter()