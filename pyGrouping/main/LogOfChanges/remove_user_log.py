import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

class UserLogApp:
    def __init__(self, notebook):
        self.tab = tk.Frame(notebook)
        notebook.add(self.tab, text="No Healthcare Account")

        # Frame for user name and phone number
        self.user_info_frame = tk.Frame(self.tab)
        self.user_info_frame.pack(padx=10, pady=10)

        # Entry for full name
        tk.Label(self.user_info_frame, text="Enter the user's full name:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.full_name_entry = tk.Entry(self.user_info_frame, width=40)
        self.full_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        # Entry for phone number
        tk.Label(self.user_info_frame, text="Enter the user's phone number:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.phone_number_entry = tk.Entry(self.user_info_frame, width=20)
        self.phone_number_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        # Button to add user
        self.add_user_button = tk.Button(self.tab, text="Add User", command=self.add_user)
        self.add_user_button.pack(pady=5)
        
        # Button to clear the entry list
        self.clear_entry_list_button = tk.Button(self.tab, text="Clear Entry List", command=self.clear_entry_list)
        self.clear_entry_list_button.pack(pady=5)
        
        # Initialize a list to store user info
        self.users = []
        self.log_message = []
        
        # Output display
        self.output_display = scrolledtext.ScrolledText(self.tab, width=50, height=10)
        self.output_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

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
        else:
            messagebox.showerror("Error", "Full name and phone number are required")
        
        self.output_display.delete("1.0", tk.END)
        for message in self.log_message:
            self.output_display.insert(tk.END, message + '\n')
            
    def clear_entry_list(self):
        self.output_display.delete("1.0", tk.END)
        self.log_message.clear()
            