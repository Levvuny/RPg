import tkinter as tk
import tkinter.ttk as tkk
from tkinter import *


window = tk.Tk()
frame = tk.Frame(master=window, width=100, height=100, bg="red")
greeting = tk.Label(text="Button Presser", master=frame)
greeting.pack()

button = tk.Button(text="Button", width=15, height=5, bg="green", fg="yellow", master=frame)
button.pack()

frame.pack(fill=tk.BOTH)
window.mainloop()
