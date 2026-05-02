import pandas as pd

df = pd.read_csv("./python/11-pandas/nba.csv")
#print(df.head())

#iterrows method
salary = []
for i, row in df.iterrows():
    s = row["Salary"]
    if pd.notnull(s) and s> 5000000:
        salary.append((row['Name'], int(s)))
for name, salary in salary[:10]:
    print(f"{name} | {salary}")

#itertuples method
for row in df.itertuples():
    print(row)  