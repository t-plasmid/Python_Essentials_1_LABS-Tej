# Author: Sgt Tej Kumar Rai
# Date Created: 28/09/2021
# Date Last Modified: 29/09/2021
# Description: The final project - Tic-Tac-Toe game.

from random import randrange

current_board_status = [[(1,1), (1,2), (1,3)], [(2,1), "X", (2,3)], [(3,1), (3,2), (3,3)]]

def start_game():
    # This function initiates the game.
    print("Welcome to the Tic-Tac-Toe game!\n\n")
    user_input = input("In the game, your move will be represented by the letter 'O,' \nwhile the computer's move will be represented by the letter 'X.' \n\n Please press enter to continue...")
    if user_input == "":
        display_board(current_board_status)
        enter_move(current_board_status)

def display_board(board):
    # This function accepts one parameter containing the board's current status and prints the current board to the console.    
    for row in range(3):
        print("\n+" + 7 * "-" + "+" + 7 * "-" + "+" + 7 * "-" + "+\n|" + 7 * " " + "|" + 7 * " " + "|" + 7 * " " + "|")
        for column in range(3):            
            if board[row][column] != 'X' and board[row][column] != 'O': print("|" + 3 * " ", (3 * (board[row][column][0] - 1) + board[row][column][1]), 3 * " ", sep="", end="")
            else: print("|" + 3 * " ", board[row][column], 3 * " ", sep="", end="")
        print("|\n|" + 7 * " " + "|" + 7 * " " + "|" + 7 * " " + "|", end="")
    print("\n+" + 7 * "-" + "+" + 7 * "-" + "+" + 7 * "-" + "+")
    
def enter_move(board):
    # This function accepts the current board status as its parameter, checks the user input, gets the user's move number, 
    # updates the current board status list and prints the current board to the console.
    user_input = 0
    wait_for_user_move = True
    while wait_for_user_move:
        wait_for_user_move = False
        try: user_input = int(input("Enter your move [1 - 9] (0 to quit):"))
        except:
            print("Invalid entry!")
            wait_for_user_move = True
            continue        
        if user_input > 0 and user_input < 10:
            if user_input >= 7:
                if board[2][user_input - 7] != "O" and board[2][user_input - 7] != "X": board[2][user_input - 7] = "O"
                else:
                    print("Invalid move!")
                    wait_for_user_move = True
            elif user_input >= 4:
                if board[1][user_input - 4] != "O" and board[1][user_input - 4] != "X": board[1][user_input - 4] = "O"
                else:                    
                    print("Invalid move!")
                    wait_for_user_move = True
            else:
                if board[0][user_input - 1] != "O" and board[0][user_input - 1] != "X": board[0][user_input - 1] = "O"
                else:                    
                    print("Invalid move!")
                    wait_for_user_move = True
        else:
            if user_input == 0: 
                wait_for_user_move = False
                continue
            else:
                print("Invalid entry!")
                wait_for_user_move = True

    if user_input != 0: display_board(current_board_status)
    if (victory_for(current_board_status, "O")): print("You won!")
    else:
        if (make_list_of_free_fields(current_board_status) > 0): 
            if user_input != 0: draw_move(current_board_status)
        else: print("Draw!")

def make_list_of_free_fields(board):
    # This function checks the current board status and builds a list of all the free squares.
    # The list consists of tuples, while each tuple is a pair of row and column numbers.    
    list_of_free_fields = []
    for row in board:
        for field in row:
            if field != "X" and field != "O": list_of_free_fields.append(field)
    return len(list_of_free_fields)

def victory_for(board, sign):
    # This function analyses the current board status to find out the winner of the game.
    won = False
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == sign: won = True
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] == sign: won = True            
    if board[0][0] == board[1][1] == board[2][2] == sign: won = True
    if board[0][2] == board[1][1] == board[2][0] == sign: won = True
    return won

def draw_move(board):
    # The function allows the computer to draw a move, updates the current board status list and prints the current board to the console.
    computer_input = 0
    wait_for_computer_move = True
    while wait_for_computer_move:
        wait_for_computer_move = False
        computer_input = int(randrange(1,10))        
        if computer_input >= 7:
            if board[2][computer_input - 7] != "O" and board[2][computer_input - 7] != "X": board[2][computer_input - 7] = "X"
            else: wait_for_computer_move = True
        elif computer_input >= 4:
            if board[1][computer_input - 4] != "O" and board[1][computer_input - 4] != "X": board[1][computer_input - 4] = "X"
            else: wait_for_computer_move = True
        else:
            if board[0][computer_input - 1] != "O" and board[0][computer_input - 1] != "X": board[0][computer_input - 1] = "X"
            else: wait_for_computer_move = True  
            
    print("Computer's move [1 - 9]:", computer_input)
    display_board(current_board_status)
    if (victory_for(current_board_status, "X")): print("Computer won!")
    else:
        if (make_list_of_free_fields(current_board_status) > 0): enter_move(current_board_status)
        else: print("Draw!")

start_game() # Entry point for the game.