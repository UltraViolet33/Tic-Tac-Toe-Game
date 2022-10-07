from re import S
from tkinter import Tk, Canvas
import random

SIZE = 300



window = Tk()
window.geometry(str(SIZE) + "x" + str(SIZE))
canvas = Canvas(window, width=SIZE, height=SIZE, borderwidth=0, highlightthickness=0, bg="lightgray")
canvas.pack()
window.mainloop()