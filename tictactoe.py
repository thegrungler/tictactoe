#! /usr/bin/env python3

from tkinter import *

board = ["","","","","","","","",""]
MAGIC_SQUARE = [4, 9, 2, 3, 5, 7, 8, 1, 6]

player = True
over = False

def check_win(player):
    count = 0
    for x in range(9):
        for y in range(9):
            for z in range(9):
                if x != y and y != z and z != x:
                    if board[x] == player and board[y] == player and board[z] == player:
                        if MAGIC_SQUARE[x] + MAGIC_SQUARE[y] + MAGIC_SQUARE[z] == 15:
                            return True
    for a in range(9):
        if board[a] == "X" or board[a] == "O":
            count += 1
        if count == 9:
            return "tie"
                        
def click(i):
    global over
    global player
    if over:
        return
    if board[i] == "":
        if player:
            board[i] = "X"
            buttons[i].configure(text = "X")
            text.configure(text = "O to play")
            player = not player
            if check_win("X"):
                over = True
                text.configure(text = "X WINS!", fg = "green")
        else:
            board[i] = "O"
            buttons[i].configure(text = "O")
            text.configure(text = "X to play")
            player = not player
            if check_win("O"):
                over = True
                text.configure(text = "O WINS!", fg = "cyan")
    if type(check_win("X")) == str:
        over = True
        text.configure(text = "TIE", fg = "red")
        
game = Tk()
game.geometry("600x700")
game.configure(bg = "#1a1a1a")
game.title("Tic Tac Toe")
game.resizable(False, False)

buttons = []

buttons.append(Button(game, text = "", font = ("Arial", 40), bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = lambda: click(0)))
buttons.append(Button(game, text = "", font = ("Arial", 40), bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = lambda: click(1)))
buttons.append(Button(game, text = "", font = ("Arial", 40), bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = lambda: click(2)))
buttons.append(Button(game, text = "", font = ("Arial", 40), bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = lambda: click(3)))
buttons.append(Button(game, text = "", font = ("Arial", 40), bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = lambda: click(4)))
buttons.append(Button(game, text = "", font = ("Arial", 40), bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = lambda: click(5)))
buttons.append(Button(game, text = "", font = ("Arial", 40), bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = lambda: click(6)))
buttons.append(Button(game, text = "", font = ("Arial", 40), bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = lambda: click(7)))
buttons.append(Button(game, text = "", font = ("Arial", 40), bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = lambda: click(8)))

text = Label(game, text = "X to play", bg = "#1a1a1a", fg = "white", anchor = "center", font = ("Arial", 20))
text.grid(row = 3, column = 1, sticky = "EW", padx = 5, pady = 5)

buttons[0].grid(column = 0, row = 0, sticky = "NSEW")
buttons[1].grid(column = 1, row = 0, sticky = "NSEW")
buttons[2].grid(column = 2, row = 0, sticky = "NSEW")
buttons[3].grid(column = 0, row = 1, sticky = "NSEW")
buttons[4].grid(column = 1, row = 1, sticky = "NSEW")
buttons[5].grid(column = 2, row = 1, sticky = "NSEW")
buttons[6].grid(column = 0, row = 2, sticky = "NSEW")
buttons[7].grid(column = 1, row = 2, sticky = "NSEW")
buttons[8].grid(column = 2, row = 2, sticky = "NSEW")

game.grid_rowconfigure(0, weight = 2)
game.grid_rowconfigure(1, weight = 2)
game.grid_rowconfigure(2, weight = 2)
game.grid_rowconfigure(3, weight = 1)
game.grid_columnconfigure(0, weight = 1)
game.grid_columnconfigure(1, weight = 1)
game.grid_columnconfigure(2, weight = 1)

game.mainloop()