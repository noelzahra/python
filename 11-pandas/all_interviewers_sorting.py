import pandas as pd
import pywhatkit


interviewers = {
    "Albert"    : 30,
    "Leo"       : 10,
    "Jean"      : 15,
    "Josef"     : 15,
    "Marzia"    : 30,
    "Michelle"  : 27
}

df = pd.read_excel("./11-pandas/Over70.xlsx")
cols = range(14,33)
df.drop(df.columns[cols], axis = 1, inplace=True)
#print(f"Total households:{df["Dwelling_HH"].count()}")

#Unique households sorted by Source
unique_hhs = df.drop_duplicates(subset=["Dwelling_HH"]).sort_values(by="Source", ascending=True)

#Save multiple households to another df
#New round robin sorting to assign interviewer to source
#Sort interviewers into a dict assignments
assignments = {}
household_list = unique_hhs["Dwelling_HH"].tolist()
household_index = 0

for interviewer, quota in interviewers.items():
    assignments[interviewer] = []
    count = 0

#Populate assignments dict
    while count < quota and household_index < len(household_list):
        assignments[interviewer].append(household_list[household_index])
        household_index += 1
        count += 1
        #print(f"Count: {count}, Household index: {household_index}")


#populate User column from assignments dict
for interviewer, houses in assignments.items():
    unique_hhs.loc[unique_hhs["Dwelling_HH"].isin(houses), "User"] = interviewer

#Add Comment column
unique_hhs["Comment"] = ""

#Save
output_path = r"NHHs-all-interviewers.xlsx"
unique_hhs.to_excel(output_path, engine="openpyxl", index=False)
report = unique_hhs.groupby(["User", "Source"])["Source"].count()

pywhatkit.sendwhatmsg('+35679798002', "All interviewers sheets are sorted by ref week", 13, 8)

print(f"Saved in : {output_path}\n\n{report}")


for interviewer, quota in interviewers.items():
    print(f"{interviewer} : {quota} households")
