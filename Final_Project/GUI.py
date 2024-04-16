import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

app = tk.Tk()
app.title("Interview Prep Software")

app.geometry('900x700')

menu_frame = tk.Frame(app, bg='#2f3d44')
main_frame = tk.Frame(app, bg='white')
header_frame = tk.Frame(app, bg='#2f3d44')

menu_frame.place(x=0,y=0,relheight=1,relwidth=0.3)
main_frame.place(relx=0.3,rely=0.1,relheight=1,relwidth=0.7)
header_frame.place(relx=0.3,y=0,relwidth=0.7,relheight=0.1)

def combobox_selected(event):
    print("Selected:", combobox.get())

combobox = ttk.Combobox(menu_frame)
combobox['values'] = ("Option 1", "Option 2", "Option 3", "Option 4")
combobox.pack(pady=10)

# Set the current value of the combobox
combobox.set("Select an option")

# Bind the selection even
combobox.bind("<<ComboboxSelected>>", combobox_selected)

app.mainloop()