import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



class MacToPhoneTab:
    def __init__(self, notebook):
        self.numbersWmac = {}
        self.tab_mac_to_phone = ttk.Frame(master=notebook)
        notebook.add(self.tab_mac_to_phone, text="MAC Addresses to Phone Numbers")
        self.setup_widgets()

    def setup_widgets(self):
        # Bulk input field and label
        tk.Label(self.tab_mac_to_phone, text="Enter phone numbers and MAC addresses (comma-separated, one pair per line):").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.bulk_entry = tk.Text(self.tab_mac_to_phone, height=10, width=50)
        self.bulk_entry.grid(row=1, column=0, padx=5, pady=5)

        # Button to add numbers
        tk.Button(self.tab_mac_to_phone, text="Add Numbers", command=self.parse_and_add_numbers).grid(row=2, column=0, padx=5, pady=5, sticky='w')
        tk.Button(self.tab_mac_to_phone, text="Clear Number history", command=lambda: self.bulk_entry.delete('1.0', tk.END)).grid(row=2, column=0, padx=5, pady=5, sticky='e')
        
        # Display field
        tk.Label(self.tab_mac_to_phone, text="Current Numbers and MACs Displayed:").grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.display = tk.Text(self.tab_mac_to_phone, height=10, width=50)
        self.display.grid(row=4, column=0, padx=5, pady=5)
        
        # button to clear display
        tk.Button(self.tab_mac_to_phone, text="Clear Display", command=lambda: self.display.delete('1.0', tk.END)).grid(row=5, column=0, padx=5, pady=5, sticky='e')
        
        # Sorted input field and label
        tk.Label(self.tab_mac_to_phone, text="Enter sorted phone numbers:").grid(row=5, column=0, padx=5, pady=5, sticky='w')
        self.sorted_entry = tk.Text(self.tab_mac_to_phone, height=5, width=50)
        self.sorted_entry.grid(row=6, column=0, padx=5, pady=5)
        
        # Button to sort and display
        tk.Button(self.tab_mac_to_phone, text="Sort and Display", command=self.sort_and_display).grid(row=7, column=0, padx=5, pady=5, sticky='w')
        tk.Button(self.tab_mac_to_phone, text="Clear Sorted", command=lambda: self.sorted_entry.delete('1.0', tk.END)).grid(row=7, column=0, padx=5, pady=5, sticky='e')
        
        # Sorted display field
        tk.Label(self.tab_mac_to_phone, text="Sorted MAC Addresses:").grid(row=8, column=0, padx=5, pady=5, sticky='w')
        self.sorted_display = tk.Text(self.tab_mac_to_phone, height=10, width=50)
        self.sorted_display.grid(row=9, column=0, padx=5, pady=5)
        
        

    def parse_and_add_numbers(self):
        input_text = self.bulk_entry.get("1.0", tk.END)
        lines = input_text.strip().split("\n")
        for line in lines:
            try:
                phone, mac = line.split(",")
                self.numbersWmac[phone.strip()] = mac.strip()
            except ValueError:
                messagebox.showerror("Error", f"Invalid input line: {line}\nPlease enter phone and MAC separated by a comma. \nExample: 1234567890, 50546461ACDE88")
        self.update_display()
        self.bulk_entry.delete('1.0', tk.END)

    def update_display(self):
        # Assuming `display` is a Text widget defined elsewhere in the class similar to `bulk_entry`
        self.display.delete('1.0', tk.END)
        self.display.insert(tk.END, "\n".join(f"{k}: {v}" for k, v in self.numbersWmac.items()))

    def sort_and_display(self):
        # Assuming `sorted_entry` and `sorted_display` are Text widgets defined elsewhere in the class
        input_text = self.sorted_entry.get("1.0", tk.END)
        sorted_list = [line.strip() for line in input_text.split('\n') if line.strip()]
        sorted_dict = {key: self.numbersWmac[key] for key in sorted_list if key in self.numbersWmac}
        self.sorted_display.delete('1.0', tk.END)
        self.sorted_display.insert(tk.END, "\n".join(sorted_dict.values()))