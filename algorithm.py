from random import randint

corners = [0, 2, 6, 8]
sides = [1, 3, 5, 7]
center = [4]
MAGIC_SQUARE = [4, 9, 2, 3, 5, 7, 8, 1, 6]

def turn(board: list, player_turn: int, opening: bool):
    if opening:
        if player_turn in center:
            return center_opener_response(board)
        if player_turn in corners or player_turn in sides:
            return other_opener_response(board)
    funny_state = funny_condition(board)
    if funny_state[2]:
        #print("condition 1")
        return funny_state
    funny_state_2 = funny_condition_2(board)
    if funny_state_2[2]:
        #print("condition 2")
        return funny_state_2
    if find_attack_space(board)[0]:
        #print("attacking")
        attack_space = attack(board)
        #print(attack_space)
        return attack_space
    if find_guard_space(board)[0]:
        #print("guarding")
        return guard(board)
    freeCorner = False
    for corner in corners:
        if board[corner] == "":
            freeCorner = True
    if freeCorner: 
        possible_tile = randint(0, 3)
        while board[corners[possible_tile]] != "":
            possible_tile = randint(0, 3)
        chosen_tile = corners[possible_tile]

        board[chosen_tile] = "O"
        return (board, chosen_tile)
    
def attack(board):
    space = find_attack_space(board)[1]
    board[space] = "O"
    return (board, space)
    
def find_attack_space(board):
    for x in range(9):
        for y in range(9):
            for z in range(9):
                if x != y and y != z and z != x:
                    if board[x] == "O" and board[y] == "O" and board[z] == "":
                        if MAGIC_SQUARE[x] + MAGIC_SQUARE[y] + MAGIC_SQUARE[z] == 15:
                            return (True, z)
    return (False, 0)
    
def funny_condition(board):
    if board == ["", "X", "", "X", "O", "", "", "", ""]:
        board = ["O", "X", "", "X", "O", "", "", "", ""]
        return (board, 0, True)
    elif board == ["", "", "", "X", "O", "", "", "X", ""]:
        board = ["", "X", "", "X", "O", "", "O", "X", ""]
        return (board, 6, True)
    elif board == ["", "X", "", "", "O", "X", "", "", ""]:
        board = ["", "X", "O", "", "O", "X", "", "", ""]
        return (board, 2, True)
    elif board == ["", "", "", "", "O", "X", "", "X", ""]:
        board = ["", "", "", "", "O", "X", "", "X", "O"]
        return (board, 8, True)
    else:
        return (board, 0, False)

def funny_condition_2(board):
    if board == ["", "X", "", "", "O", "X", "", "", ""]:
        board = ["O", "X", "", "", "O", "X", "", "", ""]
        return (board, 0, True)
    if board == ["", "", "X", "X", "O", "", "", "", ""]:
        board = ["O", "", "X", "X", "O", "", "", "", ""]
        return (board, 0, True)

    if board == ["X", "", "", "", "O", "X", "", "", ""]:
        board = ["X", "", "O", "", "O", "X", "", "", ""]
        return (board, 2, True)
    if board == ["", "X", "", "", "O", "", "", "", "X"]:
        board = ["", "X", "O", "", "O", "", "", "", "X"]
        return (board, 2, True)
    
    if board == ["", "", "", "X", "O", "", "", "", "X"]:
        board = ["", "", "", "X", "O", "", "O", "", "X"]
        return (board, 6, True)
    if board == ["X", "", "", "", "O", "", "", "X", ""]:
        board = ["X", "", "", "", "O", "", "O", "X", ""]
        return (board, 6, True)
    
    if board == ["", "", "", "", "O", "X", "X", "", ""]:
        board = ["", "", "", "", "O", "X", "X", "", "O"]
        return (board, 8, True)
    if board == ["", "", "X", "", "O", "", "", "X", ""]:
        board = ["", "", "", "", "O", "", "", "", "O"]
        return (board, 8, True)
    
    
    
    else:
        return (board, 0, False)

def guard(board):
    space = find_guard_space(board)[1]
    board[space] = "O"
    return (board, space)
    
def find_guard_space(board):
    for x in range(9):
        for y in range(9):
            for z in range(9):
                if x != y and y != z and z != x:
                    if board[x] == "X" and board[y] == "X" and board[z] == "":
                        if MAGIC_SQUARE[x] + MAGIC_SQUARE[y] + MAGIC_SQUARE[z] == 15:
                            return (True, z)
    return (False, 0)
                            
                            
                            

def center_opener_response(board):
    #generate a choice from the available tiles
    possible_tile = randint(0, 3)
    while board[corners[possible_tile]] != "":
        possible_tile = randint(0, 3)
    chosen_tile = corners[possible_tile]


    #update and return the board
    board[chosen_tile] = "O"
    return (board, chosen_tile)

def other_opener_response(board):
    board[4] = "O"
    return (board, center[0])