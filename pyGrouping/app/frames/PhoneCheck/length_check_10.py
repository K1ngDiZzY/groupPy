import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import messagebox


class PhoneNumberLengthCheckTab:
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text="Phone Number Length Check")

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
        self.num10_count_label = ttk.Label(self.scrollable_frame, text="Total 10 Digits: 0")
        self.num10_count_label.grid(row=3, column=1, padx=5, pady=5, sticky='e')
        self.big10_count_label = ttk.Label(self.scrollable_frame, text="Total > 10 Digits: 0")
        self.big10_count_label.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.small10_count_label = ttk.Label(self.scrollable_frame, text="Total <= 5 Digits: 0")
        self.small10_count_label.grid(row=4, column=1, padx=5, pady=5, sticky='e')
        self.big5_small10_count_label = ttk.Label(self.scrollable_frame, text="Total 6-10 Digits: 0")
        self.big5_small10_count_label.grid(row=5, column=0, padx=5, pady=5, sticky='w')

    def process_list(self):
        phone_numbers = self.entry.get("1.0", "end-1c").splitlines()
        phone_numbers = [num.strip() for num in phone_numbers]

        if not phone_numbers:
            messagebox.showerror("Error", "Please enter phone numbers")
            return

        num10 = [num for num in phone_numbers if len(num) == 10]
        big10 = [num for num in phone_numbers if len(num) > 10]
        small10 = [num for num in phone_numbers if len(num) < 6]
        big5_small10 = [num for num in phone_numbers if 6 <= len(num) <= 9]

        self.output_display.delete("1.0", tk.END)
        self.output_display.insert(tk.END, "Numbers that are 10 digits:\n" + "\n".join(num10) + "\n\n")
        self.output_display.insert(tk.END, "Numbers that are bigger than 10 digits:\n" + "\n".join(big10) + "\n\n")
        self.output_display.insert(tk.END, "Numbers that are smaller 6 digits:\n" + "\n".join(small10) + "\n\n")
        self.output_display.insert(tk.END, "Numbers that are between 6 and 9 digits:\n" + "\n".join(big5_small10))

        self.total_count_label.config(text=f"Total Numbers: {len(phone_numbers)}")
        self.num10_count_label.config(text=f"Total 10 Digits: {len(num10)}")
        self.big10_count_label.config(text=f"Total > 10 Digits: {len(big10)}")
        self.small10_count_label.config(text=f"Total <= 5 Digits: {len(small10)}")
        self.big5_small10_count_label.config(text=f"Total 6-9 Digits: {len(big5_small10)}")

    def clear_entry_list(self):
        self.entry.delete("1.0", tk.END)
        self.output_display.delete("1.0", tk.END)
        self.total_count_label.config(text="Total Numbers: 0")
        self.num10_count_label.config(text="Total 10 Digits: 0")
        self.big10_count_label.config(text="Total > 10 Digits: 0")
        self.small10_count_label.config(text="Total <= 5 Digits: 0")
        self.big5_small10_count_label.config(text="Total 6-10 Digits: 0")
