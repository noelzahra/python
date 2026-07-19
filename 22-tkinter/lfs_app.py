'''
    Using tkinter to build a gui application for LFS automation.
    The application will allow the user to load an .xls file from Domain and convert it to an .xlsm setup file for the Blaise app.
    To add a logging feature, withthe logging module to log events and errors. The logs can be saved to a file for later review.
    To add a notification system, we can use message boxes to inform the user of the status of the application, such as when a file is successfully loaded or if an error occurs.
    and report on teams
'''

import logging
import os
from tkinter import filedialog
import pandas as pd
from gui import LfsGUI, TextHandler

# Logging config
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    handlers=[
        logging.FileHandler("lfs_cati.log"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger(__name__)

domain_df = None  # will hold the domain DataFrame, before cleanup
df = None  # will hold the cleaned DataFrame


def load_file():
    global domain_df
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[
            ("Excel files", "*.xls *.xlsx"),
            ("All files", "*.*")
        ]
    )
    if not file_path:
        return  # user cancelled

    log.info(f"Opening '{os.path.basename(file_path)}' file")
    try:
        if file_path.lower().endswith((".xlsx", ".xls")):
            domain_df = pd.read_excel(file_path)
        else:
            domain_df = pd.read_csv(file_path)

        gui.set_status(f"Loaded: {file_path}\nRows: {len(domain_df)}, Columns: {len(domain_df.columns)}")
        gui.show_dataframe(domain_df)
        gui.enable_continue()
    except Exception as e:
        gui.show_error("Error", f"Could not load file:\n{e}")


def process_file():
    global df
    if domain_df is None:
        return

    try:
        df = domain_df.copy()

        household_hh = df['Dwelling_No'].astype(str) + '_' + df['HH_Number'].astype(str)
        person_ref = household_hh + '_' + df['personNo'].astype(str)

        # Replace the original 'Person_ref' column from the Domain file with
        # the new 'Household_HH' + 'Person_ref' columns used by DCU
        if 'Person_ref' in df.columns:
            df = df.drop(columns='Person_ref')
            log.info("Dropped Person_ref column from Domain file")

        # Build Household_HH and Person_ref columns in one pass in DataFrame
        new_cols = pd.DataFrame({'Person_ref': person_ref, 'Household_HH': household_hh})
        df = pd.concat([new_cols, df], axis=1)
        log.info("Created Household_HH and Person_ref columns according to DCU format")

        # Fill NaN values with empty strings
        df = df.fillna('').astype(str)
        df = df.apply(lambda col: col.str.replace(r'\.0', '', regex=True))
        log.info("Removed all #NULL! values")

        gui.set_status(f"Processed: Rows: {len(df)}, Columns: {len(df.columns)}")
        gui.show_dataframe(df)
    except Exception as e:
        gui.show_error("Error", f"Could not process file:\n{e}")

# Load GUI
gui = LfsGUI(on_load_file=load_file, on_continue=process_file)

text_handler = TextHandler(gui.log_text)
text_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)-8s %(message)s"))
log.addHandler(text_handler)

gui.run()
