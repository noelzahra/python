'''
    Using tkinter to build a gui application
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

    # Horizontal scrollbar in case there are many columns
    xscroll = ttk.Scrollbar(preview_frame, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=xscroll.set)

    tree.pack(fill="both", expand=True)
    xscroll.pack(fill="x")

# --- Build the GUI ---
root = tk.Tk()
root.title("Blaise Setup File Converter")
root.geometry("900x500")  # larger window to fit the preview

# Description above the button
description_label = tk.Label(
    root,
    text="Load .xls file from Domain to convert to .xlsm setup file for Blaise app.",
    font=("Segoe UI", 10, "bold")
)
description_label.pack(pady=(15, 5))

tk.Button(root, text="Load File", command=load_file, width=20).pack(pady=10)

status_label = tk.Label(root, text="No file loaded yet", wraplength=850)
status_label.pack(pady=5)

# Frame that will hold the df.head() preview
preview_frame = tk.Frame(root)
preview_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Close button pinned to the bottom right
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill="x", side="bottom", pady=10, padx=10)
tk.Button(bottom_frame, text="Close", command=root.destroy, width=12).pack(side="right")

root.mainloop()