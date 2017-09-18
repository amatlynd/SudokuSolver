#Checks the row, column and block for ith and jth indices from 0 to 81
#checks if it is in the same row
def same_row(i,j):
    return  (i/9 == j/9)

#checks in it is in the same column
def same_col(i,j):
    return ((i-j) % 9) == 0

#checks if it is in the same 3x3 block
def same_block(i,j):
    return (i/27 == j/27 and (i%9)/3 == (j%9)/3)

#returns the indexes of the static positions on a starting board
def get_static_positions(board):
    static_positions = []
    for i in range(81):
        if board[i] != '0':
            static_positions.append(i)
            
    return static_positions

#makes sublists of lists that contain values from 1 to 9
def generate_valid_values():
    values = []
    for i in range(81):
        inner = []
        for j in range(1, 10):
            inner.append(str(j))
        
        values.append(inner)
    return values
    
#checks if the board is in a winning state
def win(board):
    for i in range(81):
        for j in range(81):
            if i != j:
                if board[i] == board[j] and (same_row(i,j) or same_col(i,j) or same_block(i,j)):
                    return False
    return True
