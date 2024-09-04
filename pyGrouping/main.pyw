import tkinter as tk
from tkinter import ttk

from main.LogOfChanges.tab_generate_log import GenerateLogTab
from main.LogOfChanges.remove_user_log import UserLogApp
from main.MacAddressGui.tab_mac_to_phone import MacToPhoneTab
from main.PhoneCheck.remove_duplicate_phone_numbers import RemoveDuplicatePhoneNumbersTab
from main.PhoneCheck.skype_phone_match import PhoneNumberComparatorTab
from main.PhoneCheck.prefix_add import PhoneNumberCategorizerTab
# from main.TestingIdeas.drop_down_list_test import GenerateLogTab


def main():
    root = tk.Tk()
    root.title("Cut Sheet Helper")
    notebook = ttk.Notebook(root)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = int(screen_width * 0.3)
    window_height = int(screen_height * 0.6)

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    MacToPhoneTab(notebook)
    GenerateLogTab(notebook)
    UserLogApp(notebook)
    RemoveDuplicatePhoneNumbersTab(notebook)
    PhoneNumberComparatorTab(notebook)
    PhoneNumberCategorizerTab(notebook)

    # GenerateLogTab(notebook)

    notebook.pack(expand=1, fill="both")
    root.mainloop()


if __name__ == "__main__":
    main()
