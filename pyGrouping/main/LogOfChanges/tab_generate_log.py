import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

class GenerateLogTab:
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text='Generate Log')

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

        self.setup_widgets()

    def setup_widgets(self):
        tk.Label(self.scrollable_frame, text="Enter phone numbers:").grid(row=0, column=0, padx=10, pady=10, sticky='w')

        # Entry list setup
        self.entry_list = tk.Text(self.scrollable_frame, height=10, width=50)
        self.entry_list.grid(row=1, column=0, columnspan=2, pady=10, sticky='ew')

        tk.Label(self.scrollable_frame, text="Select the reasons for the log message:").grid(row=2, column=0, pady=10, sticky='w')

        clear_entry_button = ttk.Button(self.scrollable_frame, text="Clear Entry List", command=self.clear_entry_list)
        clear_entry_button.grid(row=2, column=1, pady=10, sticky='e')

        # Checkboxes frame
        checkboxes_frame = tk.Frame(self.scrollable_frame)
        checkboxes_frame.grid(row=3, column=0, columnspan=2, sticky='nw', padx=10)

        # Initialize variables for checkboxes
        self.var_not_found = tk.BooleanVar()
        self.var_no_bridge = tk.BooleanVar()
        self.var_removed_frm_cutsheet = tk.BooleanVar()
        self.var_speed_dial_changes = tk.BooleanVar()
        # Backburner
        self.var_backburner_device = tk.BooleanVar()
        self.var_backburner_skype = tk.BooleanVar()
        self.var_backburner_acd = tk.BooleanVar()
        self.var_backburner_not_needed = tk.BooleanVar()
        self.var_backburner_virtual = tk.BooleanVar()
        self.var_backburner_fax = tk.BooleanVar()
        self.var_backburner_hg = tk.BooleanVar()

        # Checkboxes setup within the frame using grid
        checkboxes = [
            ("Not Found in Main Cutsheet", self.var_not_found),
            ("No Bridge appearance in BR&FT", self.var_no_bridge),
            ("Speed Dial Changes", self.var_speed_dial_changes),
            ("Removed from Cutover, couldn't locate phone", self.var_removed_frm_cutsheet),
            ("Could not find Device, moved to Backburner", self.var_backburner_device),
            ("Moved Skype account to Backburner", self.var_backburner_skype),
            ("Moved ACD line to Backburner", self.var_backburner_acd),
            ("Line and phone not needed, moved to Backburner", self.var_backburner_not_needed),
            ("Virtual line not needed moved to Backburner", self.var_backburner_virtual),
            ("Fax line moved to Backburner", self.var_backburner_fax),
            ("Moved HG line to Backburner", self.var_backburner_hg),
        ]

        for i, (text, var) in enumerate(checkboxes):
            tk.Checkbutton(checkboxes_frame, text=text, variable=var).grid(row=i // 2, column=i % 2, sticky='w')

        # Result text area setup
        self.result_text_log = tk.Text(self.scrollable_frame, height=20, width=50)
        self.result_text_log.grid(row=6, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

        # Generate button setup
        generate_button = ttk.Button(self.scrollable_frame, text="Generate Log", command=self.generate_log_messages)
        generate_button.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        # Clear button setup
        clear_log_button = ttk.Button(self.scrollable_frame, text="Clear Log", command=self.clear_log)
        clear_log_button.grid(row=4, column=1, padx=10, pady=10, sticky='e')

        tk.Label(self.scrollable_frame, text="Log Messages:").grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='w')

        # Configure the column weights to allow resizing
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)

        # Configure the row weights to allow resizing
        self.scrollable_frame.grid_rowconfigure(1, weight=1)
        self.scrollable_frame.grid_rowconfigure(3, weight=1)
        self.scrollable_frame.grid_rowconfigure(4, weight=1)

    def generate_log_messages(self):
        phone_numbers = self.entry_list.get("1.0", tk.END).strip().split()
        log_messages = []
        message_templates = [
            (self.var_not_found.get(), "Removed-{number} from BR&FT since it was taken out of cut sheet and no group assigned"),
            (self.var_no_bridge.get(), "Removed-{number} from BR&FT doesn't have any bridge appearances"),
            (self.var_backburner_device.get(), "{number} - Could not find device, moved to backburner"),
            (self.var_backburner_skype.get(), "{number} - Moved skype account to backburner"),
            (self.var_backburner_acd.get(), "{number} - Moved ACD line to backburner"),
            (self.var_backburner_not_needed.get(), "{number} - Line and phone not needed anymore. Moved to Backburner."),
            (self.var_backburner_virtual.get(), "{number} - Virtual Phone line not needed and can be disconnected, moved to the backburner."),
            (self.var_backburner_fax.get(), "{number} - Moved Fax Line to Backburner"),
            (self.var_removed_frm_cutsheet.get(), "Removed - {number} from cutover, couldn't locate phone"),
            (self.var_backburner_hg.get(), "{number} - Moved HG member extension to backburner")
        ]

        for active, template in message_templates:
            if active:
                for number in phone_numbers:
                    log_messages.append(template.format(number=number))

        if self.var_speed_dial_changes.get():
            # Prompt for extension if var_speed_dial_changes is selected
            extension = simpledialog.askstring("Input", "Enter the extension for speed dial changes:")
            if extension is not None and extension != "":
                adding_comma = ', '.join(phone_numbers)
                log_messages.append(f"Removed Speed Dial(s) - {adding_comma} from extension {extension}")
            else:
                messagebox.showerror("Error", "No extension entered. Please try again.")

        self.result_text_log.delete("1.0", tk.END)

        for message in log_messages:
            self.result_text_log.insert(tk.END, message + "\n")

    def clear_log(self):
        self.result_text_log.delete("1.0", tk.END)

    def clear_entry_list(self):
        self.entry_list.delete("1.0", tk.END)
