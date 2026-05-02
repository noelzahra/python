import pandas as pd

df = pd.read_excel("./Python/11-pandas/Over70.xlsx")
cols = range(14,33)
df.drop(df.columns[cols], axis = 1, inplace=True)

#Group by unique values and sort by source
unique_hhs = df.drop_duplicates(subset=["Dwelling_HH"]).sort_values(by="Source", ascending=True,)

#adding users and iterate through list
#when array of users is more than 2 to try with itertools
users = ['Marvin', 'Josette']
unique_hhs["user"] = [users[i % 2] for i in range(len(unique_hhs))]
print(unique_hhs.head())




#Save
#unique_hhs.to_excel("./Python/11-pandas/Over70-HH-distribution.xlsx", engine="openpyxl", index=False)