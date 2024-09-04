import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Notebook with Scrollbar Example")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Create a frame for the first tab
tab1_frame = ttk.Frame(notebook)
notebook.add(tab1_frame, text="Tab 1")

# Add a Text widget to the tab frame
text_widget = tk.Text(tab1_frame, height=10, width=40)
text_widget.pack(side="left", fill="both", expand=True)

# Create a Scrollbar and set its command to the text widget's yview
scrollbar = ttk.Scrollbar(tab1_frame, orient="vertical", command=text_widget.yview)
scrollbar.pack(side="right", fill="y")

# Configure the text widget to update the scrollbar
text_widget.config(yscrollcommand=scrollbar.set)

root.mainloop()