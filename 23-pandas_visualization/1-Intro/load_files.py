"""
    Loading files in pandas is a common task when working with data. 
    Pandas can read data from different file formats such as csv, Excel, JSON, html and sql. 
"""

import pandas as pd
import lxml
import os

"""
    pandas read csv
"""
df = pd.read_csv(os.path.join('data', 'housing.csv'))
print(df.head())

#selective reading of columns
df_selected_columns = pd.read_csv(os.path.join('data', 'housing.csv'), usecols = ['Rooms', 'Price'])
print(df_selected_columns.head(10))

#to specify datatypes pass a dictionary to the dtype parameter
df_with_dtypes = pd.read_csv(os.path.join('data', 'housing.csv'), usecols = ['Rooms', 'Price'], dtype={
    'Rooms': 'int64', 
    'Price': 'float64'
    })

print(df_with_dtypes.dtypes)
print(df_with_dtypes.info())

"""
    pandas read xlsx
"""
df_households_over_70 = pd.read_excel(os.path.join('data', 'Over70.xlsx'))
print(f"Over 70 households:\n {df_households_over_70.head()}")

#reading a specific sheet
#df_sheet = pd.read_excel(os.path.join('data', 'Over70.xlsx'), sheet_name='Sheet1')
#print(f"Sheet1:\n {df_sheet.head()}")

"""
    pandas read html tables
"""
df_countries_by_population = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_population')
#print(len(df_countries_by_population))
#print(df_countries_by_population[1])