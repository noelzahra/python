import pandas as pd

df = pd.read_excel("./python/11-pandas/Over70-HH-distribution.xlsx")
#df.drop("User", axis = 1, inplace=True)
               

output_path_marvin = "./python/11-pandas/Marvin.xlsx"
output_path_josette = "./python/11-pandas/Josette.xlsx"
output_paths = [output_path_marvin, output_path_josette]

for path in output_paths:
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Marvin", index=False, )
        df.to_excel(writer, sheet_name="Josette", index=False, )

#Split dataframe into ref weeks
split_column = "RefWeekNo"
ref_week_last = 9

df_ref_week_others = df[df[split_column] != ref_week_last]
df_ref_week_last = df[df[split_column] == ref_week_last]

print(df_ref_week_others.head())
print(df_ref_week_last.head())
