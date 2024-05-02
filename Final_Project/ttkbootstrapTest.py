import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

# Create the main application window using standard Tk
root = tk.Tk()
root.title('Hybrid Application')
root.geometry('300x200')

# Standard Tkinter frame
frame = tk.Frame(root, bg='white')
frame.pack(fill='both', expand=True)

# Creating a ttkbootstrap style
style3 = tb.Style(theme='litera')

# Use the ttkbootstrap style to create a bootstrap-styled button
btn = ttk.Button(frame, text='Bootstrap Button', style='success.Outline.TButton')
btn.pack(pady=20)

style = ttk.Style(root)
style.theme_use('clam') 
# Standard ttk Button

style.configure('MenuButton.TButton', background = '#2f3d44', foreground = '#C8C8C9', width = 20, 
                borderwidth=0, focusthickness=3, focuscolor='#2f3d44', font=('Quicksand', 14, 'normal'))
style.map('MenuButton.TButton', foreground=[('active','white')], background=[('active','#2f3d44')])

analytics_header = ttk.Button(root, style='MenuButton.TButton', text="Analytics")
analytics_header.place(x=800, y=20, width=75, height=40)

standard_btn = ttk.Button(frame, text='Standard Button')
standard_btn.pack(pady=20)

root.mainloop()
