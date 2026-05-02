import pandas as pd

df = pd.read_excel("./Python/11-pandas/Over70.xlsx")
cols = range(14,33)
df.drop(df.columns[cols], axis = 1, inplace=True)

#Group by unique values and sort by source
unique_hhs = df.drop_duplicates(subset=["Dwelling_HH"]).sort_values(by="Source", ascending=True,)

#adding users and iterate through list
#when array of users is more than 2 to try with itertools
users = ['Marvin', 'Josette']
unique_hhs["User"] = [users[i % 2] for i in range(len(unique_hhs))]
unique_hhs["Comment"] = ""

#Split the dataframe into two sheets
split_column = "User"
interviewer_a = "Marvin"
interviewer_b = "Josette"

df_marvin = unique_hhs[unique_hhs[split_column] == interviewer_a]
df_josette = unique_hhs[unique_hhs[split_column] == interviewer_b]

output_path = "./Python/11-pandas/Over70-all-interviewers-distribution.xlsx"

#Save
with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    df_marvin.to_excel(writer, sheet_name=interviewer_a, index=False)
    df_josette.to_excel(writer, sheet_name=interviewer_b, index=False)

#Report
report = unique_hhs.groupby(['User', 'Source'])['Source'].count()

print(f"Saved to {output_path}\r\n{report}")