#! /usr/bin/env python3

from tkinter import *
import random
import algorithm

board = ["","","","","","","","",""]
MAGIC_SQUARE = [4, 9, 2, 3, 5, 7, 8, 1, 6]

player = True #i used a bool for this in a desperate attempt to fix bugs, doesn't affect the program just doesn't make sense
over = False
mode = "2P" #default to 2 player mode. could be changed if we feel like it
debugMode = False
opening = True

def check_win(player):
    """
    Uses a magic square to determine if the player has won. Also can return whether the game is a tie because might as well kill 2 birds with one stone
    """
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
    """
    makes the game buttons do stuff depending on whether the space is available and what mode the game is on
    """
    global over
    global board
    global opening
    if over:
        return
    if board[i] == "":
        if mode == "2P":
            two_player_turn(i)
        elif mode == "easy":
            ai_turn_easy(i)
        elif mode == "hard":
            hard_turn(i)
        opening = False
    if type(check_win("X")) == str:
        over = True
        text.configure(text = "TIE", fg = "red")

def hard_turn(i):
    global over
    global board
    board[i] = "X"
    buttons[i].configure(text = "X", fg = "green")
    if (check_win("X")):
            over = True
            text.configure(text = "X WINS!", fg = "green")
            return
    response = algorithm.turn(board, i, opening)
    if type(response) == tuple:
        board = response[0]
        buttons[response[1]].configure(text = "O", fg = "cyan")
        if (check_win("O")):
            over = True
            text.configure(text = "O WINS!", fg = "cyan")
            return
    else:
        random_space()

def two_player_turn(i):
    global player
    global over
    if player:
        board[i] = "X"
        buttons[i].configure(text = "X", fg = "green")
        text.configure(text = "O to play")
        player = not player
        if check_win("X"):
            over = True
            text.configure(text = "X WINS!", fg = "green")
    else:
        board[i] = "O"
        buttons[i].configure(text = "O", fg = "cyan")
        text.configure(text = "X to play")
        player = not player
        if check_win("O"):
            over = True
            text.configure(text = "O WINS!", fg = "cyan")


def ai_turn_easy(i):
    global over
    board[i] = "X"
    buttons[i].configure(text = "X", fg = "green")
    random_space()
    
def random_space():
    global over
    if check_win("X"):
        over = True
        text.configure(text = "X WINS!", fg = "green")
        return
    if type(check_win("X")) == str:
        over = True
        text.configure(text = "TIE", fg = "red")
        return
    while True:
        x = random.randint(0, 8)
        if board[x] == "":
            board[x] = "O"
            buttons[x].configure(text = "O", fg = "cyan")
            if check_win("O"):
                over = True
                text.configure(text = "O WINS!", fg = "green")
                return
            break
    return x

def reset():
    """
    resets everything to default values so the program doesn't become useless when a game ends
    """
    global opening
    global over
    global player
    global board
    over = False
    player = True
    opening = True
    for button in buttons:
        button.configure(text = "")
    board = ["","","","","","","","",""]
    debug()
    if mode == "2P":
        text.configure(text = "X to play", fg = "white")
    elif mode == "easy":
        text.configure(text = "Easy Mode", fg = "white")
    elif mode == "hard":
        text.configure(text = "Hard Mode", fg = "white")


def close():
    """
    just adds a close game button. nothing special
    """
    game.destroy()
        
"""
mode switching!!!!
"""
def twoPlayer():
    reset()
    global mode
    mode = "2P"
    text.configure(text = "X to play", fg = "white")

def easyMode():
    reset()
    global mode
    mode = "easy"
    text.configure(text = "Easy Mode", fg = "white")


def hardMode(): 
    reset()
    global mode
    mode = "hard"
    text.configure(text = "Hard Mode", fg = "white")

"""
creates game board
"""
game = Tk(className = "Tic Tac Toe")
game.geometry("600x800")
game.configure(bg = "#1a1a1a")
game.title("Tic Tac Toe")
game.minsize(400, 550)

photo = PhotoImage(file = "tictactoe_large.png")
game.iconphoto(False, photo)

buttons = []

"""
this could probably be done in a loop but it didn't work for me, kept passing 9 to the lambda? idk
"""
buttons.append(Button(game, text = "", font = ("Arial", 40), bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = lambda: click(0)))
buttons.append(Button(game, text = "", font = ("Arial", 40), bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = lambda: click(1)))
buttons.append(Button(game, text = "", font = ("Arial", 40), bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = lambda: click(2)))
buttons.append(Button(game, text = "", font = ("Arial", 40), bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = lambda: click(3)))
buttons.append(Button(game, text = "", font = ("Arial", 40), bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = lambda: click(4)))
buttons.append(Button(game, text = "", font = ("Arial", 40), bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = lambda: click(5)))
buttons.append(Button(game, text = "", font = ("Arial", 40), bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = lambda: click(6)))
buttons.append(Button(game, text = "", font = ("Arial", 40), bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = lambda: click(7)))
buttons.append(Button(game, text = "", font = ("Arial", 40), bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = lambda: click(8)))

"""
adds the bottom row UI elements
"""
text = Label(game, text = "X to play", bg = "#1a1a1a", fg = "white", anchor = "center", font = ("Arial", 20))
text.grid(row = 3, column = 1, sticky = "EW", padx = 5, pady = 5)

reset_button = Button(game, text = "Reset", bg = "#1f1f1f", fg = "yellow", anchor = "center", width = 10, command = reset)
reset_button.grid(column = 2, row = 3)

close_button = Button(game, text = "Quit", bg = "#1f1f1f", fg = "red", anchor = "center", width = 10, command = close)
close_button.grid(column = 0, row = 3)

twoPlayer_button = Button(game, text = "2 Player", bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = twoPlayer)
twoPlayer_button.grid(column = 0, row = 4)

easy_button = Button(game, text = "1P Easy", bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = easyMode)
easy_button.grid(column = 1, row = 4)

hard_button = Button(game, text = "1P Hard", bg = "#1f1f1f", fg = "white", anchor = "center", width = 10, command = hardMode)
hard_button.grid(column = 2, row = 4)

"""
also maybe could be done in a loop i just didnt feel like figuring out how to do it. will implement later
"""
buttons[0].grid(column = 0, row = 0, sticky = "NSEW")
buttons[1].grid(column = 1, row = 0, sticky = "NSEW")
buttons[2].grid(column = 2, row = 0, sticky = "NSEW")
buttons[3].grid(column = 0, row = 1, sticky = "NSEW")
buttons[4].grid(column = 1, row = 1, sticky = "NSEW")
buttons[5].grid(column = 2, row = 1, sticky = "NSEW")
buttons[6].grid(column = 0, row = 2, sticky = "NSEW")
buttons[7].grid(column = 1, row = 2, sticky = "NSEW")
buttons[8].grid(column = 2, row = 2, sticky = "NSEW")

def debug():
    if debugMode:
        j = 0
        while j < 9:
            buttons[j].configure(text = str(j), fg = "white")
            j+=1

"""
forces grid spaces to stay consistent with each other so the game looks pretty
"""
game.grid_rowconfigure(0, weight = 2)
game.grid_rowconfigure(1, weight = 2)
game.grid_rowconfigure(2, weight = 2)
game.grid_rowconfigure(3, weight = 1)
game.grid_rowconfigure(4, weight = 1)
game.grid_columnconfigure(0, weight = 1)
game.grid_columnconfigure(1, weight = 1)
game.grid_columnconfigure(2, weight = 1)

debug()

game.mainloop()