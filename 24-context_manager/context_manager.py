'''
Context manager is a Python feature that allows you to manage resources efficiently using the "with" statement. 
It ensures that resources are properly acquired and released, even in the presence of exceptions.
'''

#Start by using the "with" statement to open a file and automatically close it after the block of code is executed.
with open("books.txt", "w") as file:
    file.write("Book 1: The Great Gatsby\n")
    file.write("Book 2: To Kill a Mockingbird\n")
    file.write("Book 3: 1984\n")
    file.write("Book 4: Pride and Prejudice\n")
    file.write("Book 5: The Catcher in the Rye\n")
    file.write("Book 6: The Hobbit\n")
    file.write("Book 7: Fahrenheit 451\n")
    file.write("Book 8: The Lord of the Rings\n")

with open('books.txt', 'r') as file:
    titles = [line.strip().split(': ', 1)[1] for line in file]

titles.sort() # Sort the titles alphabetically

with open('catalog.txt', 'w') as catalog_file:
    for title in titles:
        catalog_file.write(title + '\n')
