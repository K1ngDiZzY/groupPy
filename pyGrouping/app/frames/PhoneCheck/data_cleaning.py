import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


class PhoneNumberCleanerGUI:
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text='Phone Number Cleaner')

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

        self.setup_widgets()

    def setup_widgets(self):
        tk.Label(self.scrollable_frame, text="Audit List (list1):").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.text_list1 = scrolledtext.ScrolledText(self.scrollable_frame, width=20, height=10)
        self.text_list1.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        tk.Label(self.scrollable_frame, text="Validation List (list2):").grid(row=0, column=1, padx=10, pady=10,
                                                                              sticky='w')
        self.text_list2 = scrolledtext.ScrolledText(self.scrollable_frame, width=20, height=10)
        self.text_list2.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

        button_clean = ttk.Button(self.scrollable_frame, text="Clean Phone Numbers", command=self.run_cleaner)
        button_clean.grid(row=2, column=0, columnspan=2, pady=10)

        # Create a frame for the results
        results_frame = tk.Frame(self.scrollable_frame)
        results_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky='nsew')

        # Create separate output boxes for each list
        self.result_matches = self.create_result_box(results_frame, "Matches", 0, 0)
        self.result_non_matches = self.create_result_box(results_frame, "Non Matches", 0, 1)
        self.result_acd_line = self.create_result_box(results_frame, "ACD Line", 0, 2)
        self.result_no_prefix = self.create_result_box(results_frame, "No Prefix", 0, 3)
        self.result_add_prefix = self.create_result_box(results_frame, "Add Prefix", 0, 4)
        self.result_cleaned_list = self.create_result_box(results_frame, "Cleaned List", 0, 5)

        tk.Label(self.scrollable_frame, text="Totals").grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='w')
        self.result_totals = scrolledtext.ScrolledText(self.scrollable_frame, width=30, height=10)
        self.result_totals.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

        # Configure the column weights to allow resizing
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)

        # Configure the row weights to allow resizing
        self.scrollable_frame.grid_rowconfigure(1, weight=1)
        self.scrollable_frame.grid_rowconfigure(3, weight=1)
        self.scrollable_frame.grid_rowconfigure(4, weight=1)

    def create_result_box(self, parent, label_text, row, column):
        tk.Label(parent, text=label_text).grid(row=row, column=column, padx=5, pady=5)
        result_box = scrolledtext.ScrolledText(parent, width=25, height=10)
        result_box.grid(row=row + 1, column=column, padx=5, pady=5)
        return result_box

    def run_cleaner(self):
        list1 = self.text_list1.get("1.0", tk.END).strip().split("\n")
        list2 = self.text_list2.get("1.0", tk.END).strip().split("\n")
        cleaner = PhoneNumberCleaner(list1, list2)
        results = cleaner.clean_phone_numbers()

        # Clear previous results
        self.clear_results()

        # Insert new results
        self.result_matches.insert(tk.END, "\n".join(results["Matches"]))
        self.result_non_matches.insert(tk.END, "\n".join(results["Non Matches"]))
        self.result_acd_line.insert(tk.END, "\n".join(results["ACD Line"]))
        self.result_no_prefix.insert(tk.END, "\n".join(results["No Prefix"]))
        self.result_add_prefix.insert(tk.END, "\n".join(results["Add Prefix"]))
        self.result_cleaned_list.insert(tk.END, "\n".join(results["Cleaned list"]))

        totals = (
            f"Matches length: {results['Matches length']}\n"
            f"Non Matches length: {results['Non Matches length']}\n"
            f"ACD Line length: {results['ACD Line length']}\n"
            f"No Prefix length: {results['No Prefix length']}\n"
            f"Add Prefix length: {results['Add Prefix length']}\n"
            f"Clean length: {results['Clean length']}\n"
            f"Duplicates removed: {results['Duplicates removed']}\n"
            f"Validation list length: {results['Validation list length']}\n"
            f"Audit list original length: {results['Audit list original length']}\n"
            f"Audit updated with no duplicates length: {results['Audit updated with no duplicates length']}\n"
            f"Difference between Updated W/O Duplicates and Clean: {results['Difference between Updated W/O Duplicates and Clean']}\n"
        )
        self.result_totals.insert(tk.END, totals)

    def clear_results(self):
        self.result_matches.delete("1.0", tk.END)
        self.result_non_matches.delete("1.0", tk.END)
        self.result_acd_line.delete("1.0", tk.END)
        self.result_no_prefix.delete("1.0", tk.END)
        self.result_add_prefix.delete("1.0", tk.END)
        self.result_cleaned_list.delete("1.0", tk.END)
        self.result_totals.delete("1.0", tk.END)


class PhoneNumberCleaner:
    def __init__(self, audit_list, validation_list):
        self.list1 = audit_list
        self.list2 = validation_list
        self.update_phone_numbers = []
        self.acd_line = []
        self.add_prefix = []
        self.no_prefix = []
        self.full_number = []
        self.matches = []
        self.non_matches = []

    def remove_duplicate_phone_numbers(self):
        unique_numbers = set(self.list1)
        self.update_phone_numbers = list(unique_numbers)
        return self.update_phone_numbers

    def remove_acd_line(self):
        self.acd_line = []
        for num in self.update_phone_numbers[:]:
            if num.startswith("209"):
                self.acd_line.append(num)
                self.update_phone_numbers.remove(num)
        return self.update_phone_numbers, self.acd_line

    def check_prefix(self):
        self.add_prefix = []
        self.no_prefix = []
        self.full_number = []

        for num in self.update_phone_numbers:
            if (num.startswith("319") or num.startswith("555")) and len(num) == 10:
                self.full_number.append(num)
            elif num.startswith("3") and len(num) == 5:
                self.add_prefix.append("31935" + num)
            elif num.startswith("4") and len(num) == 5:
                self.add_prefix.append("31938" + num)
            elif num.startswith("5") and len(num) == 5:
                self.add_prefix.append("31933" + num)
            elif num.startswith("6") and len(num) == 5:
                self.add_prefix.append("31935" + num)
            elif num.startswith("7") and len(num) == 5:
                self.add_prefix.append("31946" + num)
            elif num.startswith("8") and len(num) == 5:
                self.add_prefix.append("31967" + num)
            elif num.startswith("2") and len(num) == 5:
                self.add_prefix.append("55510" + num)
            else:
                self.no_prefix.append(num)

        for num in self.add_prefix:
            self.full_number.append(num)

        return self.no_prefix, self.full_number

    def compare_phone_numbers(self):
        self.matches = []
        self.non_matches = []

        for num1 in self.full_number:
            if num1 in self.list2:
                self.matches.append(num1)
            else:
                self.non_matches.append(num1)
        return self.matches, self.non_matches

    def clean_phone_numbers(self):
        flist1 = len(self.list1)
        flist2 = len(self.list2)

        self.remove_duplicate_phone_numbers()
        self.remove_acd_line()
        self.check_prefix()
        self.compare_phone_numbers()

        results = {
            "Matches": self.matches,
            "Non Matches": self.non_matches,
            "ACD Line": self.acd_line,
            "No Prefix": self.no_prefix,
            "Add Prefix": self.add_prefix,
            "Cleaned list": self.full_number,
            "Matches length": len(self.matches),
            "Non Matches length": len(self.non_matches),
            "ACD Line length": len(self.acd_line),
            "No Prefix length": len(self.no_prefix),
            "Add Prefix length": len(self.add_prefix),
            "Clean length": len(self.full_number),
            "Duplicates removed": flist1 - len(self.update_phone_numbers),
            "Validation list length": flist2,
            "Audit list original length": flist1,
            "Audit updated with no duplicates length": len(self.update_phone_numbers),
            "Difference between Updated W/O Duplicates and Clean": len(self.update_phone_numbers) - len(
                self.full_number)
        }

        return results
