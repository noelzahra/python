"""
This script reads the GO outgoing call log report and formats it into 
a single xlsx with interviewer name mapped to the extension in the GO report.

To add Teams notification card.
"""

from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).parent
CALL_LOG_FILE = BASE_DIR / "data" / "Outgoing - SI 26-06-26 09'32'45 1.xlsx"
EXTENSIONS_FILE = BASE_DIR / "reference_data" / "Hfcs_Interviewers_extensions.xlsx"
OUTPUT_FILE = BASE_DIR / "output" / "HFCS_formatted_call_log.xlsx"


def load_call_log(path):
    #Reading the GO outgoing report and flatten it into one table
    
    call_log = pd.read_excel(path, header=None, dtype=str)
    first_col = call_log[0].str.strip()

    # Carry each 'Extension :' number down onto the call rows below it
    is_extension_row = first_col.str.startswith("Extension", na=False)
    extension = call_log[1].where(is_extension_row).ffill()

    # Call rows are the ones where the called number is all digits
    is_call_row = first_col.str.fullmatch(r"\d+", na=False)

    # Column titles come from the first 'Called Number' row
    header_row = call_log[first_col.eq("Called Number")].iloc[0]

    calls = call_log[is_call_row].copy()
    calls.columns = header_row.str.strip()
    calls.insert(0, "Extension", extension[is_call_row].astype(int))
    return calls.reset_index(drop=True)


def load_interviewers(path):
    interviewers = pd.read_excel(path)
    return interviewers[["Extension", "CSI Name"]].rename(
        columns={"CSI Name": "Interviewer"}
    )


def main():
    calls = load_call_log(CALL_LOG_FILE)
    interviewers = load_interviewers(EXTENSIONS_FILE)

    df = calls.merge(interviewers, on="Extension", how="left")
    df["Duration"] = pd.to_timedelta(df["Duration"])
    date_hour = pd.to_datetime(df["Date/Hour"], format="%d/%m/%y %H:%M:%S")
    df["Date"] = date_hour.dt.date
    df["Hour"] = date_hour.dt.time
    df = df[["Interviewer", "Extension", "Called Number", "Duration", "Date", "Hour"]]

    unmatched = df.loc[df["Interviewer"].isna(), "Extension"].unique()
    if len(unmatched):
        print(f"No interviewer found for extension(s): {list(unmatched)}")

    print(df)

    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    save_to_excel(df, OUTPUT_FILE)
    print(f"Saved to {OUTPUT_FILE}")


def save_to_excel(df, path):
    """Write the table with Excel time and date formats on the time columns."""
    excel_df = df.copy()
    # Excel stores durations and times of day as fractions of a day
    excel_df["Duration"] = excel_df["Duration"] / pd.Timedelta(days=1)
    excel_df["Hour"] = pd.to_timedelta(excel_df["Hour"].astype(str)) / pd.Timedelta(days=1)

    formats = {"Duration": "[h]:mm:ss", "Date": "dd/mm/yyyy", "Hour": "hh:mm:ss"}
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        excel_df.to_excel(writer, index=False)
        sheet = writer.sheets["Sheet1"]
        for col_idx, name in enumerate(excel_df.columns, start=1):
            if name in formats:
                for (cell,) in sheet.iter_rows(min_row=2, min_col=col_idx, max_col=col_idx):
                    cell.number_format = formats[name]


if __name__ == "__main__":
    main()
