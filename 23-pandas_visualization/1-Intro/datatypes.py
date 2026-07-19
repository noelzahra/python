""" 
    Data Types in Pandas 
"""

import pandas as pd

#Checking datatypes of each column


fruit_series = pd.Series(['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'])

for fruit in fruit_series:
    print(f"Fruit: {fruit}, Datatype: {type(fruit)}")

fruit_data = {
    'Fruit': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'Quantity': [10, 20, 15, 5, 8],
    'Price': [0.5, 0.2, 0.75, 1.0, 1.5]
}

df_fruit = pd.DataFrame(fruit_data)
print(f"Object data Types in df_fruit:\n{df_fruit.dtypes}\n")

scores = [1, 2, 5, 8]
score_series = pd.Series(scores)
print(f"Integer data Type in score_series: {score_series.dtype}")


df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 28]
})
print(df.dtypes)

floats_df = pd.DataFrame({
    'value': [1.1, 2.2, 3.3, 4.4],
    'discount': [0.1, 0.2, 0.3, 0.4],
    'final_price': [1.0, 2.0, 3.0, 4.0]
})
print(f"Float data Types in floats_df:\n{floats_df.dtypes}\n")

bool_df = pd.DataFrame({
    'is_available': [True, False, True, True]
})
print(f"Boolean data Types in bool_df:\n{bool_df.dtypes}\n")