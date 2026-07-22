'''
Database Context Manager

This module provides a context manager for managing database connections 
and transactions. It ensures that the database connection is properly 
opened and closed, and that transactions are committed or rolled back as needed.

'''

import sqlite3

titles = [
    # list of tuples containing book titles
    (1, 'The Great Gatsby'),
    (2, 'To Kill a Mockingbird'),
    (3, '1984'),
    (4, 'Pride and Prejudice'),
    (5, 'The Catcher in the Rye'),
]


#Db context manager is a Python feature that allows you to manage database connections efficiently using the "with" statement.
with sqlite3.connect('books.db') as connection:

    # call cursor method to create a cursor object
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    ''')

    for id, title in titles:
        cursor.execute('INSERT INTO books (id, title) VALUES (?, ?)', (id, title))
    connection.commit()  # Commit the changes to the database