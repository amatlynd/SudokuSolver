from helper import *
import time
BFTotal = 0
BFnodes = 0
BFStates = []

#used for file writing
def BFreset():
    global BFStates
    global BFTotal
    global BFnodes
    BFStates = []
    BFTotal = 0
    BFnodes = 0

#fills board with 1's
def initialize_board(num):
    string_board = ""
    for i in range(81 - num):
        string_board += "1"
    return string_board
        
#finds next arrangement
def next_arrangement(string_board):
    #reverse board
    string_board = string_board[::-1]

    #try next value
    string_board = str(int(string_board) + 1)
    
    #change 0's to 1's
    for i in range(len(string_board)):
        if string_board[i] == '0':
            string_board = string_board[0:i] + '1' + string_board[i+1:]
    
    #rereverse board
    string_board = string_board[::-1]
    
    return string_board
    
#converts string board to list board
def create_board(string_board, static_positions, original_board):
    #add in static values
    for i in static_positions:
        index = int(i)
        string_board = string_board[0:index] + original_board[index] + string_board[index:]
        
    #convert string to list
    board = list(string_board)
    
    return board
    
    
#Solves the puzzle by checking all possible solutions
def brute_force(board):
    #time and node expansions    
    global BFTotal
    global BFnodes
    global BFStates
    t0 = time.time()
    
    #copy of starting board
    original_board = board[:]
    
    #finds locations of initial values
    static_positions = get_static_positions(original_board)

    #initializes board to all 1's
    string_board = initialize_board(len(static_positions))
    
    board = create_board(string_board, static_positions, original_board)
        
    #keep trying until a solution is found
    while not win(board):
        BFnodes += 1
        #try next board arrangement
        string_board = next_arrangement(string_board)
        #convert the board
        board = create_board(string_board, static_positions, original_board)
        BFStates.append(board)
        
    t1 = time.time()
    BFTotal = t1 - t0  
    
    return [board, BFTotal, BFnodes, BFStates]

