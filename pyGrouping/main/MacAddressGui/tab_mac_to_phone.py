import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MacToPhoneTab:
    def __init__(self, notebook):
        self.numbersWmac = {}
        self.tab_mac_to_phone = ttk.Frame(master=notebook)
        notebook.add(self.tab_mac_to_phone, text="MAC Addresses to Phone Numbers")

        # Create a canvas to enable scrolling
        self.canvas = tk.Canvas(self.tab_mac_to_phone)
        self.scroll_y = tk.Scrollbar(self.tab_mac_to_phone, orient="vertical", command=self.canvas.yview)
        self.scroll_x = tk.Scrollbar(self.tab_mac_to_phone, orient="horizontal", command=self.canvas.xview)
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

        # Layout for canvas and scrollbars
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scroll_y.grid(row=0, column=1, sticky="ns")
        self.scroll_x.grid(row=1, column=0, sticky="ew")

        # Configure the grid to make the canvas expandable
        self.tab_mac_to_phone.grid_rowconfigure(0, weight=1)
        self.tab_mac_to_phone.grid_columnconfigure(0, weight=1)

        self.setup_widgets()

    def setup_widgets(self):
        # Bulk input field and label
        tk.Label(self.scrollable_frame, text="Enter phone numbers and MAC addresses (comma-separated, one pair per line):").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.bulk_entry = tk.Text(self.scrollable_frame, height=10, width=50)
        self.bulk_entry.grid(row=1, column=0, padx=5, pady=5)

        # Button to add numbers
        tk.Button(self.scrollable_frame, text="Add Numbers", command=self.parse_and_add_numbers).grid(row=2, column=0, padx=5, pady=5, sticky='w')

        # Display field
        tk.Label(self.scrollable_frame, text="Current Numbers and MACs Displayed:").grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.display = tk.Text(self.scrollable_frame, height=10, width=50)
        self.display.grid(row=4, column=0, padx=5, pady=5)

        # Button to clear display
        tk.Button(self.scrollable_frame, text="Clear Display", command=self.clear_display).grid(row=5, column=0, padx=5, pady=5, sticky='e')

        # Sorted input field
        tk.Label(self.scrollable_frame, text="Enter sorted phone numbers:").grid(row=6, column=0, padx=5, pady=5, sticky='w')
        self.sorted_entry = tk.Text(self.scrollable_frame, height=5, width=50)
        self.sorted_entry.grid(row=7, column=0, padx=5, pady=5)

        # Button to sort and display
        tk.Button(self.scrollable_frame, text="Sort and Display", command=self.sort_and_display).grid(row=8, column=0, padx=5, pady=5, sticky='w')
        tk.Button(self.scrollable_frame, text="Clear Sorted Entry", command=self.clear_sorted_entry).grid(row=8, column=0, padx=5, pady=5, sticky='e')

        # Sorted display field
        tk.Label(self.scrollable_frame, text="Sorted MAC Addresses:").grid(row=9, column=0, padx=5, pady=5, sticky='w')
        self.sorted_display = tk.Text(self.scrollable_frame, height=10, width=50)
        self.sorted_display.grid(row=10, column=0, padx=5, pady=5)

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
        self.display.delete('1.0', tk.END)
        self.display.insert(tk.END, "\n".join(f"{k}: {v}" for k, v in self.numbersWmac.items()))

    def sort_and_display(self):
        input_text = self.sorted_entry.get("1.0", tk.END)
        sorted_list = [line.strip() for line in input_text.split('\n') if line.strip()]
        sorted_dict = {key: self.numbersWmac[key] for key in sorted_list if key in self.numbersWmac}
        self.sorted_display.delete('1.0', tk.END)
        self.sorted_display.insert(tk.END, "\n".join(sorted_dict.values()))

    def clear_display(self):
        self.numbersWmac.clear()
        self.update_display()
        self.display.delete('1.0', tk.END)
        
    def clear_sorted_entry(self):
        self.sorted_entry.delete('1.0', tk.END)
        self.sorted_display.delete('1.0', tk.END)
