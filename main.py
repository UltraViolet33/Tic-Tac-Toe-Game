from re import S
from tkinter import Tk, Canvas
import random

SIZE = 300

GAME = [[0, 1, 2], [0, 1, 2], [0, 1, 3]]


def displayGrid(c="black"):
    canvas.create_line((100, 0), (100, 300), width=3, fill=c)
    canvas.create_line((200, 0), (200, 300), width=3, fill=c)
    canvas.create_line((0, 100), (300, 100), width=3, fill=c)
    canvas.create_line((0, 200), (300, 200), width=3, fill=c)

def programLoop():
    displayGrid()

window = Tk()
window.geometry(str(SIZE) + "x" + str(SIZE))
canvas = Canvas(window, width=SIZE, height=SIZE, borderwidth=0,
                highlightthickness=0, bg="lightgray")
canvas.pack()
window.after(100, programLoop)
window.mainloop()
