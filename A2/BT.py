from helper import *
import time
BTStates = []
BTTotal = 0
BTnodes = 0

#used for file writing
def BTreset():
    global BTStates
    global BTTotal
    global BTnodes
    BTStates = []
    BTTotal = 0
    BTnodes = 0
    
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
    

def CSP(board):
    global BTStates
    global BTTotal
    global BTnodes
    t0 = time.time()
    valid_values = generate_valid_values()
    
    static_positions = get_static_positions(board)
    index = board.find('0')
    while index != -1:
        #find invalid values for current value
        excluded_numbers = set()
        for j in range(81):
            if same_row(index,j) or same_col(index,j) or same_block(index,j):
                excluded_numbers.add(board[j])
            
        for i in range(1,10):
            if str(i) not in valid_values[index]:
                excluded_numbers.add(str(i))
        
        #need to back track
        if len(excluded_numbers) == 10:
            #reset valid values
            valid_values[index] = ['1','2','3','4','5','6','7','8','9']

            index -= 1
            #find previous non-static position
            while index in static_positions:
                index -= 1
            #set current index to 0 
            board = board[0:index] + '0' + board[index+1:]
        else:
            for m in range(1, 10):
                if str(m) not in excluded_numbers:
                    BTnodes += 1 
                    board = board[0:index] + str(m) + board[index+1:]
                    BTStates.append(board)
                    valid_values[index].remove(str(m))
                    break
            
        index = board.find('0')

    t1 = time.time()
    BTTotal = t1 - t0

    if not win(board):
        board = -1
    return board
