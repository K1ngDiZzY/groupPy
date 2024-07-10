import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

class GenerateLogTab:
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text='Generate Log')
        self.setup_widgets()

    def setup_widgets(self):
        tk.Label(self.tab, text="Enter phone numbers:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        # Entry list setup
        self.entry_list = tk.Text(self.tab, height=10, width=50)
        self.entry_list.grid(row=2, column=0, columnspan=2, pady=10, sticky='ew')

        tk.Label(self.tab, text="Select the reasons for the log message:").grid(row=3, column=0, pady=10, sticky='w')
        
        clear_button = ttk.Button(self.tab, text="Clear Entry List", command=self.clear_entry_list)
        clear_button.grid(row=3, column=1, pady=10, sticky='e')
        
        # Checkboxes frame
        checkboxes_frame = tk.Frame(self.tab)
        checkboxes_frame.grid(row=4, column=0, sticky='nw', padx=10)
        
        # Initialize variables for checkboxes
        self.var_not_found = tk.BooleanVar()
        self.var_no_bridge = tk.BooleanVar()
        self.var_removed_frm_cutsheet = tk.BooleanVar()
        self.var_speed_dial_changes = tk.BooleanVar()
        self.var_no_healthcare = tk.BooleanVar()
        # Backburner
        self.var_backburner_device = tk.BooleanVar()
        self.var_backburner_skype = tk.BooleanVar()
        self.var_backburner_acd = tk.BooleanVar()
        self.var_backburner_not_needed = tk.BooleanVar()
        self.var_backburner_virtual = tk.BooleanVar()
        self.var_backburner_fax = tk.BooleanVar()
        self.var_backburner_hg = tk.BooleanVar()

        # Checkboxes setup within the frame using grid
        tk.Checkbutton(checkboxes_frame, text="Not Found in Main Cutsheet", variable=self.var_not_found).grid(row=0, column=0, sticky='w')
        tk.Checkbutton(checkboxes_frame, text="No Bridge appearance in BR&FT", variable=self.var_no_bridge).grid(row=1, column=0, sticky='w')
        tk.Checkbutton(checkboxes_frame, text="Speed Dial Changes", variable=self.var_speed_dial_changes).grid(row=2, column=0, sticky='w')
        tk.Checkbutton(checkboxes_frame, text="Removed from Cutover, couldn't locate phone", variable=self.var_removed_frm_cutsheet).grid(row=3, column=0, sticky='w')
        tk.Checkbutton(checkboxes_frame, text="User does not have a healthcare account", variable=self.var_no_healthcare).grid(row=4, column=0, sticky='w')
        # Backburner reasons to use
        tk.Checkbutton(checkboxes_frame, text="Could not find Device, moved to Backburner", variable=self.var_backburner_device).grid(row=0, column=1, sticky='w')
        tk.Checkbutton(checkboxes_frame, text="Moved Skype account to Backburner", variable=self.var_backburner_skype).grid(row=1, column=1, sticky='w')
        tk.Checkbutton(checkboxes_frame, text="Moved ACD line to Backburner", variable=self.var_backburner_acd).grid(row=2, column=1, sticky='w')
        tk.Checkbutton(checkboxes_frame, text="Line and phone not needed, moved to Backburner", variable=self.var_backburner_not_needed).grid(row=3, column=1, sticky='w')
        tk.Checkbutton(checkboxes_frame, text="Virtual line not needed moved to Backburner", variable=self.var_backburner_virtual).grid(row=4, column=1, sticky='w')
        tk.Checkbutton(checkboxes_frame, text="Fax line moved to Backburner", variable=self.var_backburner_fax).grid(row=5, column=1, sticky='w')
        tk.Checkbutton(checkboxes_frame, text="Moved HG line to Backburner", variable=self.var_backburner_hg).grid(row=6, column=1, sticky='w')

        # Result text area setup
        self.result_text_log = tk.Text(self.tab, height=20, width=50)
        self.result_text_log.grid(row=11, column=0, rowspan=1, pady=10, padx=10, sticky='nsew')

        # Generate button setup
        generate_button = ttk.Button(self.tab, text="Generate Log", command=self.generate_log_messages)
        generate_button.grid(row=9, column=0, padx=10, pady=10, sticky='w')
        
        # Clear button setup
        clear_button = ttk.Button(self.tab, text="Clear Log", command=self.clear_log)
        clear_button.grid(row=9, column=0, padx=10, pady=10, sticky='e')

        tk.Label(self.tab, text="Log Messages:").grid(row=10, column=0, padx=10, pady=10, sticky='w')
        
        # Configure the column weights to allow resizing
        self.tab.grid_columnconfigure(0, weight=1)
        self.tab.grid_columnconfigure(1, weight=1)
        self.tab.grid_columnconfigure(2, weight=2)
        
        #configure the row weights to allow resizing
        self.tab.grid_rowconfigure(0, weight=1)
        self.tab.grid_rowconfigure(1, weight=1)
        self.tab.grid_rowconfigure(2, weight=1)
        self.tab.grid_rowconfigure(3, weight=1)
        self.tab.grid_rowconfigure(4, weight=1)
        self.tab.grid_rowconfigure(5, weight=1)
        self.tab.grid_rowconfigure(6, weight=1)
        self.tab.grid_rowconfigure(7, weight=1)
        self.tab.grid_rowconfigure(8, weight=1)
        

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