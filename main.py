from tkinter import Tk, Canvas
import random

SIZE = 300
GAME = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def display_grid(c="black"):
    canvas.create_line((100, 0), (100, 300), width=3, fill=c)
    canvas.create_line((200, 0), (200, 300), width=3, fill=c)
    canvas.create_line((0, 100), (300, 100), width=3, fill=c)
    canvas.create_line((0, 200), (300, 200), width=3, fill=c)


def display_pawns():
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


def check_won():
    for j in [1, 2]:
        for x in range(3):
            if GAME[x][0] == GAME[x][1] == GAME[x][2] == j:
                return j
        for y in range(3):
            if GAME[0][y] == GAME[1][y] == GAME[2][y] == j:
                return j
        if GAME[0][0] == GAME[1][1] == GAME[2][2] == j:
            return j
        if GAME[0][2] == GAME[1][1] == GAME[2][0] == j:
            return j


def find_empty_cases():
    L = []
    for x in range(3):
        for y in range(3):
            if GAME[x][y] == 0:
                L.append((x, y))

    if len(L) == 0:
        return False
    else:
        i = random.randint(0, len(L) - 1)
        return L[i]


def program_loop():
    display_grid()


def display():
    canvas.delete("all")
    display_grid()
    display_pawns()


def init_game():
    global GAME
    GAME = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    display()


def click(event):
    global GAME
    display()
    x = event.x // 100
    y = event.y // 100

    if GAME[x][y] != 0:
        return

    GAME[x][y] = 1
    display_pawns()
    if check_won() == 1:
        display_grid("blue")
        window.after(3000, init_game)
        return

    computer_turn = find_empty_cases()
    if computer_turn != False:
        x, y = computer_turn
        GAME[x][y] = 2
        display_pawns()
        if check_won() == 2:
            display_grid("red")
            window.after(3000, init_game)
            return


window = Tk()
window.geometry(str(SIZE) + "x" + str(SIZE))
canvas = Canvas(window, width=SIZE, height=SIZE, borderwidth=0,
                highlightthickness=0, bg="lightgray")
canvas.pack()
window.after(100, program_loop)
window.bind("<Button-1>", click)
window.mainloop()
