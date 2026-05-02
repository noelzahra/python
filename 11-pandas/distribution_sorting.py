import pandas as pd

#Over70.xlsx
df = pd.read_excel(r"Over70.xlsx")
cols = range(14,33)
df.drop(df.columns[cols], axis = 1, inplace=True)

#Group by unique values and sort by source
unique_hhs = df.drop_duplicates(subset=["Dwelling_HH"]).sort_values(by="Source", ascending=True)

#adding users and iterate through list
#when array of users is more than 2 to try with itertools
users = ['Marvin', 'Josette']
unique_hhs["User"] = [users[i % 2] for i in range(len(unique_hhs))]
unique_hhs["Comment"] = ""

output_path = r"Over70-all-interviewers-distribution.xlsx"
unique_hhs.to_excel(output_path, engine="openpyxl", index=False)

#Report
report = unique_hhs.groupby(['User', 'Source'])['Source'].count()
total_count = unique_hhs["Dwelling_HH"].count()


print(f"Saved to {output_path}\r\n{report}\r\nTotal households distributed:{total_count}")