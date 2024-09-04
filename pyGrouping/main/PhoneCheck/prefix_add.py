import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import messagebox


class PhoneNumberCategorizerTab:
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text="Phone Number Categorizer")

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
        ttk.Label(self.phone_numbers_frame, text="Enter Phone Numbers (one number per line):").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entry = tk.Text(self.phone_numbers_frame, height=10, width=50)
        self.entry.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        # Button to process list
        self.process_button = ttk.Button(self.scrollable_frame, text="Process List", command=self.process_list)
        self.process_button.grid(row=1, column=0, pady=5, sticky='w')

        # Button to clear the entry list
        self.clear_entry_list_button = ttk.Button(self.scrollable_frame, text="Clear Entry List", command=self.clear_entry_list)
        self.clear_entry_list_button.grid(row=1, column=1, pady=5, sticky='e')

        # Output display
        self.output_display = scrolledtext.ScrolledText(self.scrollable_frame, width=50, height=10)
        self.output_display.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        # Labels for counts
        self.total_count_label = ttk.Label(self.scrollable_frame, text="Total Numbers: 0")
        self.total_count_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.already_has_prefix_count_label = ttk.Label(self.scrollable_frame, text="Total with Prefix: 0")
        self.already_has_prefix_count_label.grid(row=3, column=1, padx=5, pady=5, sticky='e')
        self.need_prefix_count_label = ttk.Label(self.scrollable_frame, text="Total Need Prefix: 0")
        self.need_prefix_count_label.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.no_prefix_count_label = ttk.Label(self.scrollable_frame, text="Total No Prefix: 0")
        self.no_prefix_count_label.grid(row=4, column=1, padx=5, pady=5, sticky='e')

    def categorize_phone_numbers(self, phone_numbers):
        already_has_prefix = []
        need_prefix = []
        no_prefix = []

        for num in phone_numbers:
            if num.startswith("319") or num.startswith("555"):
                already_has_prefix.append(num)
            elif num.startswith("3"):
                need_prefix.append("31935" + num)
            elif num.startswith("4"):
                need_prefix.append("31938" + num)
            elif num.startswith("5"):
                need_prefix.append("31933" + num)
            elif num.startswith("6"):
                need_prefix.append("31935" + num)
            elif num.startswith("7"):
                need_prefix.append("31946" + num)
            elif num.startswith("8"):
                need_prefix.append("31967" + num)
            elif num.startswith("2") and len(num) == 5:
                need_prefix.append("55510" + num)
            else:
                no_prefix.append(num)

        return already_has_prefix, need_prefix, no_prefix

    def process_list(self):
        phone_numbers = self.entry.get("1.0", "end-1c").splitlines()
        phone_numbers = [num.strip() for num in phone_numbers]

        if not phone_numbers:
            messagebox.showerror("Error", "Please enter phone numbers")
            return

        already_has_prefix, need_prefix, no_prefix = self.categorize_phone_numbers(phone_numbers)

        self.output_display.delete("1.0", tk.END)
        self.output_display.insert(tk.END, "Phone Numbers with Prefix:\n" + "\n".join(already_has_prefix) + "\n\n")
        self.output_display.insert(tk.END, "Phone Numbers Need Prefix:\n" + "\n".join(need_prefix) + "\n\n")
        self.output_display.insert(tk.END, "Phone Numbers No Prefix:\n" + "\n".join(no_prefix))

        self.total_count_label.config(text=f"Total Numbers: {len(phone_numbers)}")
        self.already_has_prefix_count_label.config(text=f"Total with Prefix: {len(already_has_prefix)}")
        self.need_prefix_count_label.config(text=f"Total Need Prefix: {len(need_prefix)}")
        self.no_prefix_count_label.config(text=f"Total No Prefix: {len(no_prefix)}")

    def clear_entry_list(self):
        self.entry.delete("1.0", tk.END)
        self.output_display.delete("1.0", tk.END)
        self.total_count_label.config(text="Total Numbers: 0")
        self.already_has_prefix_count_label.config(text="Total with Prefix: 0")
        self.need_prefix_count_label.config(text="Total Need Prefix: 0")
        self.no_prefix_count_label.config(text="Total No Prefix: 0")