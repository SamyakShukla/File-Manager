


import webbrowser 
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
ROOT = tk.Tk()
ROOT.withdraw()
def open_pdff():
    location= simpledialog.askstring(title="PDF to open",
                                  prompt="Location of PDF file to Open:")
    webbrowser.get('windows-default').open(location)
    messagebox.showinfo("PDF file opened","PDF file opened on your default Browser")
#open_pdff()







