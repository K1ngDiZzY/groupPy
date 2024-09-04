import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

root = tk.Tk("Phone Number Log Generator")
root.title("Cut Sheet Helper")
notebook = ttk.Notebook(master=root)
notebook.grid(row=0, column=0, padx=10, pady=10)


def generate_log_messages():
    phone_numbers = entry_list.get("1.0", tk.END).strip().split()
    log_messages = []
    message_templates = [
        (var_not_found.get(), "Removed - {number} from BR&FT since it was taken out of cut sheet and no group assigned"),
        (var_no_bridge.get(), "Removed - {number} from BR&FT doesn't have any bridge appearances"),
        (var_backburner_device.get(), "{number} - Could not find device, moved to backburner"),
        (var_backburner_skype.get(), "{number} - Moved skype account to backburner"),
        (var_backburner_acd.get(), "{number} - Moved ACD line to backburner"),
        (var_backburner_not_needed.get(), "{number} - Line and phone not needed anymore. Moved to Backburner."),
        (var_backburner_virtual.get(), "{number} - Virtual Phone line not needed and can be disconnected, moved to the backburner."),
        (var_backburner_fax.get(), "{number} - Moved Fax Line to Backburner"),
        (var_removed_frm_cutsheet.get(), "Removed - {number} from cutover, couldn't locate phone"),
        (var_backburner_hg.get(), "{number} - Moved HG member extension to backburner")
    ]

    for active, template in message_templates:
        if active:
            for number in phone_numbers:
                log_messages.append(template.format(number=number))

    if var_speed_dial_changes.get():
        # Prompt for extension if var_speed_dial_changes is selected
        extension = simpledialog.askstring("Input", "Enter the extension for speed dial changes:")
        if extension is not None and extension != "":  # Check if an extension was entered
            adding_comma = ', '.join(phone_numbers)
            log_messages.append(f"Removed Speed Dial(s) - {adding_comma} from extension {extension}")
        else:
            messagebox.showerror("Error", "No extension entered. Please try again.")
            

    result_text_log.delete("1.0", tk.END)
    for message in log_messages:
        result_text_log.insert(tk.END, message + "\n")

def clear_log():
    result_text_log.delete("1.0", tk.END)

def parse_and_add_numbers():
    input_text = bulk_entry.get("1.0", tk.END)
    lines = input_text.strip().split("\n")
    for line in lines:
        try:
            phone, mac = line.split(",")
            numbersWmac[phone.strip()] = mac.strip()
        except ValueError:
            print("Skipping invalid line:", line)
    update_display()
    bulk_entry.delete('1.0', tk.END)
    
def update_display():
    display.delete('1.0', tk.END)
    display.insert(tk.END, "\n".join(f"{k}: {v}" for k, v in numbersWmac.items()))

def sort_and_display():
    input_text = sorted_entry.get("1.0", tk.END)
    sorted_list = [line.strip() for line in input_text.split('\n') if line.strip()]
    sorted_dict = {key: numbersWmac[key] for key in sorted_list if key in numbersWmac}
    sorted_display.delete('1.0', tk.END)
    sorted_display.insert(tk.END, "\n".join(sorted_dict.values()))
    
    

# Tab 1: Generate Log Messages
tab_generate_log = ttk.Frame(master=notebook)
notebook.add(tab_generate_log, text="Generate Log Messages")

entry_label = ttk.Label(tab_generate_log, text="Enter phone numbers:")
entry_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_list = tk.Text(tab_generate_log, width=75, height=10)
entry_list.grid(row=1, column=0, padx=1, pady=5)

# Create Checkbuttons for each log option
# Non-Backburner reasons to use
var_not_found = tk.BooleanVar()
check_not_found = ttk.Checkbutton(tab_generate_log, text="Not found in main cutsheet, no group", variable=var_not_found)
check_not_found.grid(row=4, column=0, padx=2, pady=2, sticky="w")

var_no_bridge = tk.BooleanVar()
check_no_bridge = ttk.Checkbutton(tab_generate_log, text="No bridge appearance in BR&FT", variable=var_no_bridge)
check_no_bridge.grid(row=5, column=0, padx=2, pady=2, sticky="w")

var_speed_dial_changes = tk.BooleanVar()
check_speed_dial_changes = ttk.Checkbutton(tab_generate_log, text="Speed Dial(s) Remove", variable=var_speed_dial_changes)
check_speed_dial_changes.grid(row=6, column=0, padx=2, pady=2, sticky="w")

var_removed_frm_cutsheet = tk.BooleanVar()
removed_frm_cutsheet = ttk.Checkbutton(tab_generate_log, text="Removed from cutover, couldn't locate phone", variable=var_removed_frm_cutsheet)
removed_frm_cutsheet.grid(row=7, column=0, padx=2, pady=2, sticky="w")


# Backburner reasons to use
var_backburner_device = tk.BooleanVar()
check_backburner_device = ttk.Checkbutton(tab_generate_log, text="Could not find device, moved to backburner", variable=var_backburner_device)
check_backburner_device.grid(row=4, column=1, padx=2, pady=2, sticky="w")

var_backburner_skype = tk.BooleanVar()
check_backburner_skype = ttk.Checkbutton(tab_generate_log, text="Moved skype account to backburner", variable=var_backburner_skype)
check_backburner_skype.grid(row=5, column=1, padx=2, pady=2, sticky="w")

var_backburner_acd = tk.BooleanVar()
check_backburner_acd = ttk.Checkbutton(tab_generate_log, text="Moved ACD line to backburner", variable=var_backburner_acd)
check_backburner_acd.grid(row=6, column=1, padx=2, pady=2, sticky="w")

var_backburner_not_needed = tk.BooleanVar()
check_backburner_not_needed = ttk.Checkbutton(tab_generate_log, text="Line and phone not needed, moved to Backburner", variable=var_backburner_not_needed)
check_backburner_not_needed.grid(row=7, column=1, padx=2, pady=2, sticky="w")

var_backburner_virtual = tk.BooleanVar()
check_backburner_virtual = ttk.Checkbutton(tab_generate_log, text="Virtual phone line not needed, moved to backburner", variable=var_backburner_virtual)
check_backburner_virtual.grid(row=8, column=1, padx=2, pady=2, sticky="w")

var_backburner_fax = tk.BooleanVar()
check_backburner_fax = ttk.Checkbutton(tab_generate_log, text="Moved Fax Line to Backburner", variable=var_backburner_fax)
check_backburner_fax.grid(row=9, column=1, padx=2, pady=2, sticky="w")

var_backburner_hg = tk.BooleanVar()
check_backburner_hg = ttk.Checkbutton(tab_generate_log, text="Moved HG member ext to backburner", variable=var_backburner_hg)
check_backburner_hg.grid(row=10, column=1, padx=2, pady=2, sticky="w")

# Button to generate log messages
display_button_log = ttk.Button(tab_generate_log, text="Generate Logs", command=generate_log_messages)
display_button_log.grid(row=11, column=0, padx=5, pady=5)

display_clear_log = ttk.Button(tab_generate_log, text="Clear logs", command=clear_log)
display_clear_log.grid(row=11, column=1, padx=5, pady=5)

# Result label and text widget for log messages
result_label_log = ttk.Label(tab_generate_log, text="Log Messages:")
result_label_log.grid(row=12, column=0, padx=5, pady=5, sticky="w")
result_text_log = tk.Text(tab_generate_log, width=100, height=15)
result_text_log.grid(row=13, column=0, padx=5, pady=5)



# Tab 2: MAC Addresses to Phone Numbers
tab_mac_to_phone = ttk.Frame(master=notebook)
notebook.add(tab_mac_to_phone, text="MAC Addresses to Phone Numbers")

numbersWmac = {}

# Bulk input field and label
tk.Label(tab_mac_to_phone, text="Enter phone numbers and MAC addresses (comma-separated, one pair per line):").grid(row=0, column=0, padx=5, pady=5)
bulk_entry = tk.Text(tab_mac_to_phone, height=10, width=50)
bulk_entry.grid(row=1, column=0, padx=5, pady=5)

# Button to add numbers
tk.Button(tab_mac_to_phone, text="Add Numbers", command=parse_and_add_numbers).grid(row=2, column=0, padx=5, pady=5)

# Display area for current numbers and MACs
tk.Label(tab_mac_to_phone, text="Current Numbers and MACs:").grid(row=3, column=0, padx=5, pady=5)
display = tk.Text(tab_mac_to_phone, height=10, width=50)
display.grid(row=4, column=0, padx=5, pady=5)

# Input and button for sorting
tk.Label(tab_mac_to_phone, text="Enter sorted phone numbers:").grid(row=5, column=0, padx=5, pady=5)
sorted_entry = tk.Text(tab_mac_to_phone, height=5, width=50)
sorted_entry.grid(row=6, column=0, padx=5, pady=5)
tk.Button(tab_mac_to_phone, text="Sort and Display", command=sort_and_display).grid(row=7, column=0, padx=5, pady=5)

# Sorted display area
tk.Label(tab_mac_to_phone, text="Sorted MAC Addresses:").grid(row=8, column=0, padx=5, pady=5)
sorted_display = tk.Text(tab_mac_to_phone, height=10, width=50)
sorted_display.grid(row=9, column=0, padx=5, pady=5)



# Start the main event loop
root.mainloop()