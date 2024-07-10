import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

from main.LogOfChanges.tab_generate_log import GenerateLogTab
from main.LogOfChanges.remove_user_log import UserLogApp
from main.MacAddressGui.tab_mac_to_phone import MacToPhoneTab

def main():
    root = tk.Tk()
    root.title("Cut Sheet Helper")
    notebook = ttk.Notebook(root)

    generate_ordered_macs = MacToPhoneTab(notebook)
    generate_log_tab = GenerateLogTab(notebook)
    generate_Old_user_tab = UserLogApp(notebook)

    notebook.pack(expand=1, fill="both")
    root.mainloop()

if __name__ == "__main__":
    main()