from helper import *
import time
FCStates = []
FCTotal = 0
FCnodes = 0

#used for file writing
def FCreset():
    global FCStates
    global FCTotal
    global FCnodes
    FCStates = []
    FCTotal = 0
    FCnodes = 0
    
#finds the next index for MRV
def find_next_position(board, valid_values):
    #default value
    index = -1
    
    indexes = []
    #find indexes of empty spaces and store them
    for i in range(81):
        if board[i] == '0':
            indexes.append(i)
    
    min_num = 999
    #minimum value heuristic for possible values
    for i in indexes:
        if len(valid_values[i]) < min_num:
            index = i
            min_num = len(valid_values[i])

    return index

#updates the valid moves
def update_valid_values(board):
    new_list = generate_valid_values()
    for i in range(81):
        for j in range(81):
            if same_row(i,j) or same_col(i,j) or same_block(i,j):
                if board[j] in new_list[i]:
                    new_list[i].remove(board[j])
    return new_list

#make 81 empty sublists
def generate_blacklist_values():
    lst = []
    for i in range(81):
        lst.append([])
    return lst
    
#remove blacklisted_values
def remove_blacklist_values(valid_values, blacklist_values):
    for i in range(81):
        for value in blacklist_values[i]:
            if value in valid_values[i]:
                valid_values[i].remove(value)
    return valid_values

#checks if any square has an invalid move
def backtrack(board, valid_values):
    for i in range(81):
        if board[i] == '0' and len(valid_values[i]) == 0:
            return True
    return False


def FC_MRV(board):
    global FCStates
    global FCTotal
    global FCnodes
    t0 = time.time()

    valid_values = update_valid_values(board)
    
    #used for backtracking
    blacklist_values = generate_blacklist_values()
    stack = []
    
    index = find_next_position(board, valid_values)
    while index != -1:    
        #need to back track
        if backtrack(board, valid_values):
            #reset valid values
            valid_values[index] = ['1','2','3','4','5','6','7','8','9']
            blacklist_values[index] = []
            
            #set previous index to 0 
            prev_index = stack.pop()
            board = board[0:prev_index] + '0' + board[prev_index+1:]
            
            index = prev_index
            
        else:
            for m in valid_values[index]:
                FCnodes += 1
                
                #add value to current index
                board = board[0:index] + m + board[index+1:]
                FCStates.append(board)
                #add blacklisted value
                blacklist_values[index].append(m)
                #add history to stack
                stack.append(index)
                #find next index using MRV
                index = find_next_position(board, valid_values)
                break
                
        #update valid values
        valid_values = update_valid_values(board)
        valid_values = remove_blacklist_values(valid_values, blacklist_values)
    t1 = time.time()
    FCTotal = t1 - t0
    
    if not win(board):
        board = -1
        
    return board
