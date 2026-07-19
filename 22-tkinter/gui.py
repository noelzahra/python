'''
    Tkinter GUI for LFS app.
    Builds the main window, tabs, and treeview/log widgets.
    Business logic (loading and cleaning the DataFrame) lives in lfs_app.py,
    which drives this module through the LfsGUI interface below.
'''

import logging
import os
import tomllib
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.scrolledtext import ScrolledText

with open(os.path.join(os.path.dirname(__file__), "pyproject.toml"), "rb") as f:
    __version__ = tomllib.load(f)["project"]["version"]


class TextHandler(logging.Handler):
    # Logging handler that appends formatted log records to a Tkinter Text widget.
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text_widget.configure(state="normal")
            self.text_widget.insert("end", msg + "\n")
            self.text_widget.configure(state="disabled")
            self.text_widget.see("end")
        # Route through Tk's event loop so this is safe even if logged from another thread
        self.text_widget.after(0, append)


class LfsGUI:
    # Creates the main window and all its widgets, including treeview setup/logic.
    def __init__(self, on_load_file, on_continue):
        self.root = tk.Tk()
        self.root.title("LFS Setup File Converter")
        self.root.geometry("1000x600")
        self.root.minsize(1000, 600)
        self.root.resizable(True, True)

        # Bring window to the front on launch
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.after(100, lambda: self.root.attributes("-topmost", False))
        self.root.focus_force()

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True)

        self._build_cati_tab(notebook, on_load_file, on_continue)
        self._build_capi_tab(notebook)
        self._build_audits_tab(notebook)
        self.log_text = self._build_logs_tab(notebook)

    def _build_cati_tab(self, notebook, on_load_file, on_continue):
        cati_tab = ttk.Frame(notebook)
        notebook.add(cati_tab, text="CATI")

        tk.Label(
            cati_tab,
            text="Load .xls file from Domain to convert to .xlsm setup file\n for the management.msu module in the Blaise app.",
            font=("Segoe UI", 10, "bold")
        ).pack(pady=(15, 5))

        button_bar = tk.Frame(cati_tab)
        button_bar.pack(pady=10)

        tk.Button(button_bar, text="Load File", command=on_load_file, width=20).pack(side="left", padx=5)

        self.continue_button = tk.Button(
            button_bar, text="Continue", command=on_continue, width=20, state="disabled"
        )
        self.continue_button.pack(side="left", padx=5)

        self.status_label = tk.Label(cati_tab, text="No file loaded yet", wraplength=850)
        self.status_label.pack(pady=5)

        # Frame that will hold the df.head() preview
        self.preview_frame = tk.Frame(cati_tab)
        self.preview_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Bottom bar: version label on the left, Close button on the right
        cati_bottom = tk.Frame(cati_tab)
        cati_bottom.pack(fill="x", side="bottom", pady=10, padx=10)

        tk.Label(cati_bottom, text=f"DCU tools v{__version__}", fg="gray").pack(side="left")
        tk.Button(cati_bottom, text="Close", command=self.root.destroy, width=12).pack(side="right")

    def _build_capi_tab(self, notebook):
        capi_tab = ttk.Frame(notebook)
        notebook.add(capi_tab, text="CAPI")

        tk.Label(
            capi_tab,
            text="CAPI panel — coming soon",
            font=("Segoe UI", 10, "bold")
        ).pack(pady=20)

    def _build_audits_tab(self, notebook):
        audits_tab = ttk.Frame(notebook)
        notebook.add(audits_tab, text="Audits")

        tk.Label(
            audits_tab,
            text="Load .xls file from Domain to convert to .xlsm setup file\n for the management.msu module in the Blaise app.",
            font=("Segoe UI", 10, "bold")
        ).pack(pady=20)

    def _build_logs_tab(self, notebook):
        logs_tab = ttk.Frame(notebook)
        notebook.add(logs_tab, text="Logs")

        log_text = ScrolledText(logs_tab, state="disabled", wrap="word", font=("Consolas", 9))
        log_text.pack(fill="both", expand=True, padx=10, pady=10)
        return log_text

    def set_status(self, text):
        self.status_label.config(text=text)

    def enable_continue(self):
        self.continue_button.config(state="normal")

    def disable_continue(self):
        self.continue_button.config(state="disabled")

    def show_dataframe(self, df):
        # Clear any previous output
        for widget in self.preview_frame.winfo_children():
            widget.destroy()

        # Populate the CATI preview frame with a Treeview of df.head(20).
        head = df.head(20)

        tree = ttk.Treeview(
            self.preview_frame,
            columns=list(head.columns),
            show="headings",
            height=6
        )
        for col in head.columns:
            tree.heading(col, text=col)
            tree.column(col, width=120, anchor="w")

        for _, row in head.iterrows():
            tree.insert("", "end", values=list(row))

        xscroll = ttk.Scrollbar(self.preview_frame, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=xscroll.set)

        tree.pack(fill="both", expand=True)
        xscroll.pack(fill="x")

    def show_error(self, title, message):
        messagebox.showerror(title, message)

    def run(self):
        self.root.mainloop()
