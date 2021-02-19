from PIL import Image
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog
from mergepdf import merge
from tkinter import messagebox
import os
ROOT = tk.Tk()
ROOT.withdraw()
def i_to_pdf():
    location= simpledialog.askstring(title="Image to Pdf",
                                  prompt="Location of Image to be converted:")    
    filename =location
    # the image to be converted should be from the root directory and enter the name of the image here
    img = Image.open(filename, "r")
    if img.mode == "RGBA":
        img = img.convert("RGB")
    output = str(datetime.now().strftime("%Y%m%d-%H%M%S"))+"output.pdf"
    # file name is output.pdf with the date and time including minutes and seconds
    img.save(output, "PDF", resolution=100.0)
    print("PDF Successfully converted from image file")    
    messagebox.showinfo("Image to Pdf","PDF Successfully converted from image file")





