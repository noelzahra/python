import pandas as pd

df = pd.read_excel(r"NHHs-all-interviewers.xlsx", index_col=False)
#df.drop("User", axis = 1, inplace=True)
               
each_interviewer = df["User"].unique()

for interviewer in each_interviewer:
    df_interviewer = df[df["User"] == interviewer]
    output_path = f"./11-pandas/{interviewer}.xlsx"

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:

        #Split dataframe into ref weeks
        split_column = "RefWeekNo"
        ref_week_last = 9

        #Report
        report = df_interviewer.groupby(['User', 'Source'])['Source'].count()

        #Drop User col
        df_interviewer.drop("User", axis = 1, inplace=True)
        

        #Split ref weeks
        df_ref_week_others = df_interviewer[df_interviewer[split_column] != ref_week_last].sort_values(by="Dwelling_HH", ascending=True)
        df_ref_week_last = df_interviewer[df_interviewer[split_column] == ref_week_last].sort_values(by="Dwelling_HH", ascending=True)

        #Save worksheets by ref week
        df_ref_week_others.to_excel(writer, sheet_name = f"Ref_week-{ref_week_last - 4}, {ref_week_last - 3}, {ref_week_last - 2}, {ref_week_last - 1}")
        df_ref_week_last.to_excel(writer, sheet_name = f"Ref_week-{ref_week_last}")
        
        print(f"Saved to {output_path}\r\n{report}")
