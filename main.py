from tkinter import Tk, Canvas
import random

from matplotlib.pyplot import eventplot

SIZE = 300
GAME = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def displayGrid(c="black"):
    canvas.create_line((100, 0), (100, 300), width=3, fill=c)
    canvas.create_line((200, 0), (200, 300), width=3, fill=c)
    canvas.create_line((0, 100), (300, 100), width=3, fill=c)
    canvas.create_line((0, 200), (300, 200), width=3, fill=c)
    
    
def displayPawns():
    for x in range(3):
        for y in range(3):
            xx = x * 100
            yy = y * 100
            A = (xx + 20, yy + 20)
            B = (xx + 80, yy + 80)
            C = (xx + 20, yy + 80)
            D = (xx + 80, yy + 20)
            
            if GAME[x][y] == 1:
                canvas.create_oval(A, B, fill="blue")
            if GAME[x][y] == 2:
                canvas.create_line(A, B, fill="red", width=10)
                canvas.create_line(C, D, fill="red", width=10)


def checkWon():
    for j in [1, 2]:
        for x in range(3):
            if GAME[x][0] == GAME[x][1] == GAME[x][2] == j : return j
        for y in range(3):
            if GAME[0][y] == GAME[1][y] == GAME[2][y] == j : return j
        if GAME[0][0] == GAME[1][1] == GAME[2][2] == j : return j
        if GAME[0][2] == GAME[1][1] == GAME[2][0] == j : return j
        
        
def findEmptyCases():
    L = []
    for x in range(3):
        for y in range(3):
            if GAME[x][y] == 0:
                L.append((x, y))
                
    if len(L) == 0: return False  
    else:
        i = random.randint(0, len(L) - 1)
        return L[i]


def programLoop():
    displayGrid()



def display():
    canvas.delete("all")
    displayGrid()
    displayPawns()
                

def click(event):
    global GAME
    display()
    x = event.x // 100
    y = event.y // 100
    
    # if checkWon() != 0:
    #     GAME = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    #     display()
    #     return 
    
    if GAME[x][y] != 0 : return 
    
    GAME[x][y] = 1
    displayPawns()
    if checkWon() == 1:
        displayGrid("blue")
        return 
    
    computer_turn = findEmptyCases()
    if computer_turn != False:
        x, y = computer_turn
        GAME[x][y] = 2
        displayPawns()
        if checkWon() == 2:
            displayGrid("red")
            return 





window = Tk()
window.geometry(str(SIZE) + "x" + str(SIZE))
canvas = Canvas(window, width=SIZE, height=SIZE, borderwidth=0,
                highlightthickness=0, bg="lightgray")
canvas.pack()
window.after(100, programLoop)
window.bind("<Button-1>", click)
window.mainloop()
