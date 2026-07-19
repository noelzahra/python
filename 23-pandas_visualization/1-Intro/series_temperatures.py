"""
    Pandas basics
"""

import pandas as pd

"""
    Series are one dimensional array-like objects that can hold any data type. 
    They are similar to NumPy arrays, but they have additional functionality, 
    such as the ability to label the data with an index.
"""

temperatures = [25, 28, 30, 26, 29, 31, 27]

series = pd.Series(temperatures)
print(series)


#Repeat same value of 10, index starts from 0 to 6
value = 10
series_of_10 = pd.Series(value, index=range(7))
print(series_of_10)

#assign custom labels to the index
ages = [25, 30, 35, 28, 32]
index_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
ages_series = pd.Series(ages, index=index_names)

for name, age in ages_series.items():
    print(f"{name}: {age} years")