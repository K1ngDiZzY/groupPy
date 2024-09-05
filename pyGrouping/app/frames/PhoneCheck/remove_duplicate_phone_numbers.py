import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import messagebox


class RemoveDuplicatePhoneNumbersTab:
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text="Remove Duplicate Phone Numbers")

        # Create a canvas to enable scrolling
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

        # Layout for canvas and scrollbars
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scroll_y.grid(row=0, column=1, sticky="ns")
        self.scroll_x.grid(row=1, column=0, sticky="ew")

        # Configure the grid to make the canvas expandable
        self.tab.grid_rowconfigure(0, weight=1)
        self.tab.grid_columnconfigure(0, weight=1)

        # Frame for phone numbers
        self.phone_numbers_frame = ttk.Frame(self.scrollable_frame)
        self.phone_numbers_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        # Entry for phone numbers
        ttk.Label(self.phone_numbers_frame, text="Enter Phone Numbers (one number per line):").grid(row=0, column=0,
                                                                                                    padx=5, pady=5,
                                                                                                    sticky='w')
        self.entry = tk.Text(self.phone_numbers_frame, height=10, width=50)
        self.entry.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        # Button to process list
        self.process_button = ttk.Button(self.scrollable_frame, text="Process List", command=self.process_list)
        self.process_button.grid(row=1, column=0, pady=5, sticky='w')

        # Button to clear the entry list
        self.clear_entry_list_button = ttk.Button(self.scrollable_frame, text="Clear Entry List",
                                                  command=self.clear_entry_list)
        self.clear_entry_list_button.grid(row=1, column=1, pady=5, sticky='e')

        # Output display
        self.output_display = scrolledtext.ScrolledText(self.scrollable_frame, width=50, height=10)
        self.output_display.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        # Labels for counts
        self.total_count_label = ttk.Label(self.scrollable_frame, text="Total Numbers: 0")
        self.total_count_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.unique_count_label = ttk.Label(self.scrollable_frame, text="Total Unique Numbers: 0")
        self.unique_count_label.grid(row=3, column=1, padx=5, pady=5, sticky='e')

    def remove_duplicate_phone_numbers(self, phone_numbers):
        unique_numbers = set(phone_numbers)
        unique_list = list(unique_numbers)
        return unique_list

    def process_list(self):
        phone_numbers = self.entry.get("1.0", "end-1c").splitlines()
        phone_numbers = [num.strip() for num in phone_numbers]

        if not phone_numbers:
            messagebox.showerror("Error", "Please enter phone numbers")
            return

        unique_phone_numbers = self.remove_duplicate_phone_numbers(phone_numbers)

        self.output_display.delete("1.0", tk.END)
        self.output_display.insert(tk.END, "Unique Phone Numbers:\n" + "\n".join(unique_phone_numbers))

        self.total_count_label.config(text=f"Total Numbers: {len(phone_numbers)}")
        self.unique_count_label.config(text=f"Total Unique Numbers: {len(unique_phone_numbers)}")

    def clear_entry_list(self):
        self.entry.delete("1.0", tk.END)
        self.output_display.delete("1.0", tk.END)
        self.total_count_label.config(text="Total Numbers: 0")
        self.unique_count_label.config(text="Total Unique Numbers: 0")
