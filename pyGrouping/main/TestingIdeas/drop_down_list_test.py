# import tkinter as tk
# from tkinter import ttk
# from tkinter import simpledialog
# from tkinter import messagebox

# class GenerateLogTab:
#     def __init__(self, notebook):
#         self.tab = ttk.Frame(notebook)
#         notebook.add(self.tab, text='Generate Log')

#         # Create a canvas to enable scrolling
#         self.canvas = tk.Canvas(self.tab)
#         self.scroll_y = tk.Scrollbar(self.tab, orient="vertical", command=self.canvas.yview)
#         self.scroll_x = tk.Scrollbar(self.tab, orient="horizontal", command=self.canvas.xview)
#         self.scrollable_frame = ttk.Frame(self.canvas)

#         self.scrollable_frame.bind(
#             "<Configure>",
#             lambda e: self.canvas.configure(
#                 scrollregion=self.canvas.bbox("all")
#             )
#         )

#         self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
#         self.canvas.configure(yscrollcommand=self.scroll_y.set)
#         self.canvas.configure(xscrollcommand=self.scroll_x.set)

#         # Layout for canvas and scrollbars
#         self.canvas.grid(row=0, column=0, sticky="nsew")
#         self.scroll_y.grid(row=0, column=1, sticky="ns")
#         self.scroll_x.grid(row=1, column=0, sticky="ew")

#         # Configure the grid to make the canvas expandable
#         self.tab.grid_rowconfigure(0, weight=1)
#         self.tab.grid_columnconfigure(0, weight=1)

#         self.setup_widgets()

#     def setup_widgets(self):
#         tk.Label(self.scrollable_frame, text="Enter phone numbers:").grid(row=0, column=0, padx=10, pady=10, sticky='w')

#         # Entry list setup
#         self.entry_list = tk.Text(self.scrollable_frame, height=10, width=50)
#         self.entry_list.grid(row=1, column=0, columnspan=2, pady=10, sticky='ew')

#         tk.Label(self.scrollable_frame, text="Select the reasons for the log message:").grid(row=2, column=0, pady=10, sticky='w')

#         clear_entry_button = ttk.Button(self.scrollable_frame, text="Clear Entry List", command=self.clear_entry_list)
#         clear_entry_button.grid(row=2, column=1, pady=10, sticky='e')

#         # Checkboxes frame
#         checkboxes_frame = tk.Frame(self.scrollable_frame)
#         checkboxes_frame.grid(row=3, column=0, columnspan=2, sticky='nw', padx=10)

#         # Initialize variables for checkboxes
        
#         # Add
#         self.var_add_virtualLine_HG = tk.BooleanVar()
#         self.var_add_voicemail_to_phone = tk.BooleanVar()
#         self.var_add_phone_BRFT = tk.BooleanVar()
#         self.var_add_phone_to_HG = tk.BooleanVar()
#         self.var_add_call_forward = tk.BooleanVar()
#         self.var_add_bridge = tk.BooleanVar()
        
#         # update
#         self.var_update_userAD = tk.BooleanVar()
#         self.var_update_userFirst_lastName = tk.BooleanVar()
#         self.var_update_userEmail = tk.BooleanVar()
#         self.var_update_phone_location = tk.BooleanVar()
#         self.var_update_phone_Mac = tk.BooleanVar()
        
        
#         #remove
#         self.var_removed_not_found = tk.BooleanVar()
#         self.var_removed_no_bridge = tk.BooleanVar()
#         self.var_removed_speed_dial_changes = tk.BooleanVar()
#         self.var_removed_backburner_device = tk.BooleanVar()
#         self.var_removed_backburner_skype = tk.BooleanVar()
#         self.var_removed_backburner_acd = tk.BooleanVar()
#         self.var_removed_backburner_not_needed = tk.BooleanVar()
#         self.var_removed_backburner_virtual = tk.BooleanVar()
#         self.var_removed_backburner_fax = tk.BooleanVar()
#         self.var_removed_backburner_hg = tk.BooleanVar()
        

#         # Checkboxes setup within the frame using grid
#         checkboxes = [
            
#             # Add
#             ("Add Virtual Line for HG", self.var_add_virtualLine_HG),
#             ("Add Voicemail to Phone", self.var_add_voicemail_to_phone),
#             ("Add Phone to BR&FT", self.var_add_phone_BRFT),
#             ("Add Phone to HG Main Line", self.var_add_phone_to_HG),
#             ("Add Call Forwarding", self.var_add_call_forward),
#             ("Add Bridge Appearance", self.var_add_bridge),
                        
#             #update
#             ("Update User's AD name", self.var_update_userAD),
#             ("Update User's First and Last name", self.var_update_userFirst_lastName),
#             ("Update User's Email", self.var_update_userEmail),
#             ("Update Phone Location", self.var_update_phone_location),
#             ("Update Phone MAC Address", self.var_update_phone_Mac),
            
            
            
#             # remove
#             ("Phone not found in Main Cutsheet", self.var_removed_not_found),
#             ("No Bridge appearance in BR&FT", self.var_removed_no_bridge),
#             ("Speed Dial Changes", self.var_removed_speed_dial_changes),
#             ("Could not find Device, moved to Backburner", self.var_removed_backburner_device),
#             ("Moved Skype account to Backburner", self.var_removed_backburner_skype),
#             ("Moved ACD line to Backburner", self.var_removed_backburner_acd),
#             ("Line and phone not needed, moved to Backburner", self.var_removed_backburner_not_needed),
#             ("Virtual line not needed moved to Backburner", self.var_removed_backburner_virtual),
#             ("Fax line moved to Backburner", self.var_removed_backburner_fax),
#             ("Moved HG line to Backburner", self.var_removed_backburner_hg),
#         ]

#         for i, (text, var) in enumerate(checkboxes):
#             tk.Checkbutton(checkboxes_frame, text=text, variable=var).grid(row=i // 2, column=i % 2, sticky='w')

#         # Result text area setup
#         self.result_text_log = tk.Text(self.scrollable_frame, height=20, width=50)
#         self.result_text_log.grid(row=6, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

#         # Generate button setup
#         generate_button = ttk.Button(self.scrollable_frame, text="Generate Log", command=self.generate_log_messages)
#         generate_button.grid(row=4, column=0, padx=10, pady=10, sticky='w')

#         # Clear button setup
#         clear_log_button = ttk.Button(self.scrollable_frame, text="Clear Log", command=self.clear_log)
#         clear_log_button.grid(row=4, column=1, padx=10, pady=10, sticky='e')

#         tk.Label(self.scrollable_frame, text="Log Messages:").grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='w')

#         # Configure the column weights to allow resizing
#         self.scrollable_frame.grid_columnconfigure(0, weight=1)
#         self.scrollable_frame.grid_columnconfigure(1, weight=1)

#         # Configure the row weights to allow resizing
#         self.scrollable_frame.grid_rowconfigure(1, weight=1)
#         self.scrollable_frame.grid_rowconfigure(3, weight=1)
#         self.scrollable_frame.grid_rowconfigure(4, weight=1)

#     def generate_log_messages(self):
#         phone_numbers = self.entry_list.get("1.0", tk.END).strip().split()
#         log_messages = []
#         message_templates = [
            
#             # ADD list
#             (self.var_add_virtualLine_HG.get(), "Added - Created virtual line for HG {number}"),
#             (self.var_add_voicemail_to_phone.get(), "Added - Voicemail to {number}"),
#             (self.var_add_phone_BRFT.get(), "Added - Added {number} to BR&FT"),
            
#             # Update list
#             (self.var_update_userAD.get(), "Updated - User's AD name for {number} "),
#             (self.var_update_userFirst_lastName.get(), "Updated - User's First and Last name for {number}"),
#             (self.var_update_userEmail.get(), "Updated - User's Email for {number}"),
            
#             # Remove List
#             (self.var_removed_not_found.get(), "Removed - {number} from BR&FT since it was taken out of cutsheet and no group assigned"),
#             (self.var_removed_no_bridge.get(), "Removed - {number} from BR&FT doesn't have any bridge appearances"),
#             (self.var_removed_backburner_device.get(), "Removed - Could not locate {number} , moved to backburner"),
#             (self.var_removed_backburner_skype.get(), "Removed - {number} moved skype account to backburner"),
#             (self.var_removed_backburner_acd.get(), "Removed - {number} moved ACD line to backburner"),
#             (self.var_removed_backburner_not_needed.get(), "Removed - {number} not needed anymore. Moved to Backburner."),
#             (self.var_removed_backburner_virtual.get(), "Removed - {number} Virtual Phone line not needed, moved to the backburner."),
#             (self.var_removed_backburner_fax.get(), "Removed - {number} moved Fax Line to Backburner"),
#             (self.var_removed_backburner_hg.get(), "Removed - {number} moved HG member extension to backburner")
#         ]

#         for active, template in message_templates:
#             if active:
#                 for number in phone_numbers:
#                     log_messages.append(template.format(number=number))
        
#         if self.var_add_phone_to_HG.get():
#             # Prompt for extension if var_add_phone_to_HG is selected
#             extension = simpledialog.askstring("Input", "Enter the extension for HG main line:")
#             if extension is not None and extension != "":
#                 adding_comma = ', '.join(phone_numbers)
#                 log_messages.append(f"Added - Added {adding_comma} to HG main line extension {extension}")
#             else:
#                 messagebox.showerror("Error", "No extension entered. Please try again.")
                
#         if self.var_add_call_forward.get():
#             # Prompt for extension if var_add_call_forward is selected
#             forwardNumber = simpledialog.askstring("Input", "Enter the number to forward to:")
#             if forwardNumber is not None and forwardNumber != "":
#                 adding_comma = ', '.join(phone_numbers)
#                 log_messages.append(f"Added - Call Forwarding for {adding_comma} to {forwardNumber}")
#             else:
#                 messagebox.showerror("Error", "No number entered. Please try again.")
        
#         if self.var_add_bridge.get():
#             # Prompt for extension if var_add_bridge is selected
#             bridgeNumber = simpledialog.askstring("Input", "Enter the number to bridge to:")
#             if bridgeNumber is not None and bridgeNumber != "":
#                 adding_comma = ', '.join(phone_numbers)
#                 log_messages.append(f"Added - Bridge appearance for {adding_comma} to {bridgeNumber}")
#             else:
#                 messagebox.showerror("Error", "No number entered. Please try again.")
        
#         if self.var_update_phone_location.get():
#             # Prompt for extension if var_update_phone_location is selected
#             oldLocation = simpledialog.askstring("Input", "Enter the old location:")
#             newLocation = simpledialog.askstring("Input", "Enter the new location:")
#             if oldLocation is not None and oldLocation != "" and newLocation is not None and newLocation != "":
#                 adding_comma = ', '.join(phone_numbers)
#                 log_messages.append(f"Updated - Phone Location for {adding_comma} old location {oldLocation}, new location {newLocation}")
#             else:
#                 messagebox.showerror("Error", "No location entered. Please try again.")
                
#         if self.var_update_phone_Mac.get():
#             # Prompt for extension if var_update_phone_Mac is selected
#             oldMac = simpledialog.askstring("Input", "Enter the old MAC Address:")
#             newMac = simpledialog.askstring("Input", "Enter the new MAC Address:")
#             if oldMac is not None and oldMac != "" and newMac is not None and newMac != "":
#                 adding_comma = ', '.join(phone_numbers)
#                 log_messages.append(f"Updated - Phone MAC Address for {adding_comma}, old MAC Address {oldMac}, new MAC Address {newMac}")
#             else:
#                 messagebox.showerror("Error", "No MAC Address entered. Please try again.")
                

#         if self.var_removed_speed_dial_changes.get():
#             # Prompt for extension if var_speed_dial_changes is selected
#             extension = simpledialog.askstring("Input", "Enter the extension for speed dial changes:")
#             if extension is not None and extension != "":
#                 adding_comma = ', '.join(phone_numbers)
#                 log_messages.append(f"Removed - Speed Dial(s) {adding_comma} from extension {extension}")
#             else:
#                 messagebox.showerror("Error", "No extension entered. Please try again.")
        

#         self.result_text_log.delete("1.0", tk.END)

#         for message in log_messages:
#             self.result_text_log.insert(tk.END, message + "\n")

#     def clear_log(self):
#         self.result_text_log.delete("1.0", tk.END)

#     def clear_entry_list(self):
#         self.entry_list.delete("1.0", tk.END)
