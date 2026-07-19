"""
    DataFrames are two-dimensional, size-mutable, and heterogeneous tabular data structures 
    with labeled axes (rows and columns).
    DataFrames can be thought of as a collection of Series objects that share the same index.
    DataFrames structure consists of data, index, and columns.
"""
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)
print(df)

#customing index and columns
custom_index = ['A', 'B', 'C', 'D', 'E']
custom_df = pd.DataFrame(data, index=custom_index, columns=['Name', 'Age', 'City'])
print(custom_df)
