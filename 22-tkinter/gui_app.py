'''
    Using tkinter to build a gui application for LFS automation. 
    The application will allow the user to load a .xls file from Domain and convert it to a .xlsm setup file for the Blaise app.
    To add a logging feature, we can use the logging module to log events and errors. The logs can be saved to a file for later review.
    To add a notification system, we can use message boxes to inform the user of the status of the application, such as when a file is successfully loaded or if an error occurs.
    and report on teams
'''

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

df = None  # will hold the loaded DataFrame

def load_file():
    global df
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[
            ("Excel files", "*.xls *.xlsx"),
            ("All files", "*.*")
        ]
    )
    if not file_path:
        return  # user cancelled

    try:
        if file_path.lower().endswith((".xlsx", ".xls")):
            df = pd.read_excel(file_path)
        else:
            df = pd.read_csv(file_path)

        status_label.config(
            text=f"Loaded: {file_path}\nRows: {len(df)}, Columns: {len(df.columns)}"
        )
        show_head(df)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load file:\n{e}")

def show_head(df):
    # Clear any previous output
    for widget in preview_frame.winfo_children():
        widget.destroy()

    head = df.head()

    tree = ttk.Treeview(
        preview_frame,
        columns=list(head.columns),
        show="headings",
        height=6
    )
    for col in head.columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="w")

    for _, row in head.iterrows():
        tree.insert("", "end", values=list(row))

    xscroll = ttk.Scrollbar(preview_frame, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=xscroll.set)

    tree.pack(fill="both", expand=True)
    xscroll.pack(fill="x")

# --- Build the main window ---
root = tk.Tk()
root.title("LFS Setup File Converter")
root.geometry("1000x600")

# Bring window to the front on launch
root.lift()
root.attributes("-topmost", True)
root.after(100, lambda: root.attributes("-topmost", False))
root.focus_force()

# --- Notebook (tab container) ---
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# ============ CATI tab ============
cati_tab = ttk.Frame(notebook)
notebook.add(cati_tab, text="CATI")

description_label = tk.Label(
    cati_tab,
    text="Load .xls file from Domain to convert to .xlsm setup file\n for the management.msu module in the Blaise app.",
    font=("Segoe UI", 10, "bold")
)
description_label.pack(pady=(15, 5))

tk.Button(cati_tab, text="Load File", command=load_file, width=20).pack(pady=10)

status_label = tk.Label(cati_tab, text="No file loaded yet", wraplength=850)
status_label.pack(pady=5)

# Frame that will hold the df.head() preview
preview_frame = tk.Frame(cati_tab)
preview_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Bottom bar: version label on the left, Close button on the right
cati_bottom = tk.Frame(cati_tab)
cati_bottom.pack(fill="x", side="bottom", pady=10, padx=10)

version_label = tk.Label(cati_bottom, text="DCU tools v1.0 beta", fg="gray")
version_label.pack(side="left")

tk.Button(cati_bottom, text="Close", command=root.destroy, width=12).pack(side="right")

# ============ CAPI tab (blank for now) ============
capi_tab = ttk.Frame(notebook)
notebook.add(capi_tab, text="CAPI")

tk.Label(capi_tab, text="CAPI panel — coming soon").pack(pady=20)

root.mainloop()