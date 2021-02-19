from PIL import Image
import tkinter as tk
from tkinter import simpledialog
from mergepdf import merge
from tkinter import messagebox
ROOT = tk.Tk()
ROOT.withdraw()
def open_image():
    location= simpledialog.askstring(title="Open Image",
                                  prompt="Image Location:")

    img=Image.open(location)#file should be from the current working directory and this file only for test purpose
    messagebox.showinfo("Image format",img.format)   
    messagebox.showinfo("Image Dimensions",img.size)
    img.show()#shows image
    rotated=img.rotate(90)#rotates image to 90 degree
    rotated.show()#shows rotated image
    more_rotate=rotated.rotate(90)#rotates the previously rotated image
    more_rotate.show()#shows the new rotated image
    new_img=Image.open(location).convert('L')#converts image to grey scale
    new_img.show() #shows new grey scale image
    new_img.save(location)#saves the new rotated and grey scaled image


import tkinter as tk
from tkinter import simpledialog
from mergepdf import merge
from tkinter import messagebox
ROOT = tk.Tk()

ROOT.withdraw()

def merge_window():
    location_1= simpledialog.askstring(title="PDF Merge",
                                  prompt="First PDF Location:")
    location_2= simpledialog.askstring(title="PDF Merge",
                                  prompt="Second PDF Location:")
    merge(location_1,location_2)
    messagebox.showinfo("File merged","File merged")
    merge(location_1,location_2)





#import Pillow to do image processing
from PIL import Image
def open_image():
    location= simpledialog.askstring(title="Open Image",
                                  prompt="Image Location:")

    img=Image.open(location)#file should be from the current working directory and this file only for test purpose
    messagebox.showinfo("Image format",img.format)   
    messagebox.showinfo("Image size",img.size)
    print(img.format)#prints image format
    print(img.size)#prints image size
    img.show()#shows image
    rotated=img.rotate(90)#rotates image to 90 degree
    rotated.show()#shows rotated image
    more_rotate=rotated.rotate(90)#rotates the previously rotated image
    more_rotate.show()#shows the new rotated image
    new_img=Image.open(location).convert('L')#converts image to grey scale
    new_img.show() #shows new grey scale image
    new_img.save(location)#saves the new rotated and grey scaled image

