import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

class UserLogApp:
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text="No Healthcare Account")

        self.canvas = tk.Canvas(self.tab)
        self.scroll_y = tk.Scrollbar(self.tab, orient="vertical", command=self.canvas.yview)
        self.scroll_x = tk.Scrollbar(self.tab, orient="horizontal", command=self.canvas.xview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scroll_y.set)
        self.canvas.configure(xscrollcommand=self.scroll_x.set)

        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scroll_y.grid(row=0, column=1, sticky="ns")
        self.scroll_x.grid(row=1, column=0, sticky="ew")
        
        self.tab.grid_rowconfigure(0, weight=1)
        self.tab.grid_columnconfigure(0, weight=1)
        

        self.user_info_frame = ttk.Frame(self.scrollable_frame)
        self.user_info_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        # Entry for full name
        ttk.Label(self.user_info_frame, text="Enter the user's full name:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.full_name_entry = ttk.Entry(self.user_info_frame, width=40)
        self.full_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        # Entry for phone number
        ttk.Label(self.user_info_frame, text="Enter the user's phone number:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.phone_number_entry = ttk.Entry(self.user_info_frame, width=20)
        self.phone_number_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        # Button to add user
        self.add_user_button = ttk.Button(self.scrollable_frame, text="Add User", command=self.add_user)
        self.add_user_button.grid(row=1, column=0, pady=5, sticky='w')

        # Button to clear the entry list
        self.clear_entry_list_button = ttk.Button(self.scrollable_frame, text="Clear Entry List", command=self.clear_entry_list)
        self.clear_entry_list_button.grid(row=1, column=1, pady=5, sticky='e')

        # Initialize a list to store user info
        self.users = []
        self.log_message = []

        # Output display
        self.output_display = scrolledtext.ScrolledText(self.scrollable_frame, width=50, height=10)
        self.output_display.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

    def add_user(self):
        full_name = self.full_name_entry.get().strip()
        phone_number = self.phone_number_entry.get().strip()
        if full_name and phone_number:
            # Combine full name and phone number into a dictionary and add to the list
            self.users.append({"full_name": full_name, "phone_number": phone_number})
            print("Added user:", self.users[-1])  # For demonstration, print the last added user
            message_template = f"{phone_number} - Removed from Cutover, {full_name} doesn't have a healthcare account"
            self.log_message.append(message_template)
            # Optionally clear the entries after adding
            self.full_name_entry.delete(0, tk.END)
            self.phone_number_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Full name and phone number are required")

        self.output_display.delete("1.0", tk.END)
        for message in self.log_message:
            self.output_display.insert(tk.END, message + '\n')

    def clear_entry_list(self):
        self.output_display.delete("1.0", tk.END)
        self.log_message.clear()
