"""
 Using pandas DataFrame and Series
    1. A single column of data froma DataFrame is returned as a Series
    2. A Series is a one-dimensional array with axis labels
    3. A Series method can return another Series as output
    4. A Series can support method chaining. Series.method1().method2()...methodN()

Dataframe: A table of rows and columns
    1. A DataFrame has three main components: data (referred as values), index, and columns, which are all mutable. 
"""

import pandas as pd
import os

# movies is a DataFrame
movies = pd.read_csv(os.path.join("..", "data", "movie.csv"))
print([movies.head(), movies.tail()])

# director_name is a Series, one column of the DataFrame movies
director_name = movies['director_name']
print(director_name.head())

#Value datatype in movies DataFrame 
#print(movies.dtypes)

# genre is another Series, one column of the DataFrame movies
genre = movies['genres']
print(genre.head())

# Count values in a Series
directors_count = director_name.count()
print(f"Number of directors: {directors_count}")

genre_count = genre.count()
print(f"Number of genres: {genre_count}" )
