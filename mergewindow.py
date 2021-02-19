


import tkinter as tk
from tkinter import simpledialog
from mergepdf import merge
from tkinter import messagebox
ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
def merge_window():
    location_1= simpledialog.askstring(title="PDF Merge",
                                  prompt="First PDF Location:")
    location_2= simpledialog.askstring(title="PDF Merge",
                                  prompt="Second PDF Location:")
    merge(location_1,location_2)
    messagebox.showinfo("File merged","File merged")
# check it out
    #print("Hello", location_1,location_2)
    merge(location_1,location_2)
#merge_window()







