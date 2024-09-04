import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import messagebox


class PhoneNumberComparatorTab:
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text="Phone Number Comparator")

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
        ttk.Label(self.phone_numbers_frame, text="Enter List 1 (one number per line):").grid(row=0, column=0, padx=5,
                                                                                             pady=5, sticky='w')
        self.entry1 = tk.Text(self.phone_numbers_frame, height=10, width=50)
        self.entry1.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        self.list1_count_label = ttk.Label(self.phone_numbers_frame, text="Total in List 1: 0")
        self.list1_count_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        ttk.Label(self.phone_numbers_frame, text="Enter List 2 (one number per line):").grid(row=3, column=0, padx=5,
                                                                                             pady=5, sticky='w')
        self.entry2 = tk.Text(self.phone_numbers_frame, height=10, width=50)
        self.entry2.grid(row=4, column=0, padx=5, pady=5, sticky='w')

        self.list2_count_label = ttk.Label(self.phone_numbers_frame, text="Total in List 2: 0")
        self.list2_count_label.grid(row=5, column=0, padx=5, pady=5, sticky='w')

        # Button to compare lists
        self.compare_button = ttk.Button(self.scrollable_frame, text="Compare", command=self.compare_phone_numbers)
        self.compare_button.grid(row=1, column=0, pady=5, sticky='w')

        # Button to clear the entry list
        self.clear_entry_list_button = ttk.Button(self.scrollable_frame, text="Clear Entry List",
                                                  command=self.clear_entry_list)
        self.clear_entry_list_button.grid(row=1, column=1, pady=5, sticky='e')

        # Output display
        self.output_display = scrolledtext.ScrolledText(self.scrollable_frame, width=50, height=10)
        self.output_display.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        # Labels for counts
        self.matches_count_label = ttk.Label(self.scrollable_frame, text="Total Matches: 0")
        self.matches_count_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.non_matches_count_label = ttk.Label(self.scrollable_frame, text="Total Non-Matches: 0")
        self.non_matches_count_label.grid(row=3, column=1, padx=5, pady=5, sticky='e')
        self.acd_line_count_label = ttk.Label(self.scrollable_frame, text="Total ACD Line: 0")
        self.acd_line_count_label.grid(row=4, column=0, padx=5, pady=5, sticky='w')

    def compare_phone_numbers(self):
        list1 = self.entry1.get("1.0", "end-1c").splitlines()
        list2 = self.entry2.get("1.0", "end-1c").splitlines()

        list1 = [num.strip() for num in list1]
        list2 = [num.strip() for num in list2]

        matches = []
        non_matches = []
        acd_line = []

        last5_list2 = [num[-5:] for num in list2]

        for num1 in list1:
            if num1.startswith("209"):
                acd_line.append(num1)
            elif num1[-5:] in last5_list2:
                matches.append(num1)
            else:
                non_matches.append(num1)

        self.output_display.delete("1.0", tk.END)
        self.output_display.insert(tk.END, "Matching Numbers:\n" + "\n".join(matches) + "\n\n")
        self.output_display.insert(tk.END, "Non-Matching Numbers:\n" + "\n".join(non_matches) + "\n\n")
        self.output_display.insert(tk.END, "ACD Line (Numbers starting with 209):\n" + "\n".join(acd_line))

        self.list1_count_label.config(text=f"Total in List 1: {len(list1)}")
        self.list2_count_label.config(text=f"Total in List 2: {len(list2)}")
        self.matches_count_label.config(text=f"Total Matches: {len(matches)}")
        self.non_matches_count_label.config(text=f"Total Non-Matches: {len(non_matches)}")
        self.acd_line_count_label.config(text=f"Total ACD Line: {len(acd_line)}")

    def clear_entry_list(self):
        self.entry1.delete("1.0", tk.END)
        self.entry2.delete("1.0", tk.END)
        self.output_display.delete("1.0", tk.END)
        self.list1_count_label.config(text="Total in List 1: 0")
        self.list2_count_label.config(text="Total in List 2: 0")
        self.matches_count_label.config(text="Total Matches: 0")
        self.non_matches_count_label.config(text="Total Non-Matches: 0")
        self.acd_line_count_label.config(text="Total ACD Line: 0")
