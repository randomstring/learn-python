#!/usr/bin/python3
#
# Sudoku Solver
#

size = 9

def print_board(board):
    for (i,row) in enumerate(board):
        print("row", (i+1), ":",end="")
        for val in row:
            if val == 0:
                print(" . ",end="")
            else:
                print(" ",val," ",end="",sep="")
        print("")

def empty_board(size): return [ [ 0 for i in range(size)] for i in range(size)]

def populate_board(board, entries):
    # entry is a list [ x, y, value ]
    for entry in entries:
        [x, y, val] = entry
        board[x][y] = val

board = empty_board(9)

# From The Algorithm Design Manual 2nd Edition (S. S. Skiena) Page 239
# this is a "hard" problem
populate_board(board,[[0,7,1],[0,8,2],[1,4,3],[1,5,5],[2,3,6],[2,7,7],[3,0,7],[3,6,3],[4,3,4],[4,6,8],[5,0,1],[6,3,1],[6,4,2],[7,1,8],[7,7,4],[8,1,5],[8,6,6]])

# hint
populate_board(board,[[0,0,6],[0,1,7],[0,2,3],[1,0,9],[2,0,8]])

solution = ["6 7 3 8 9 4 5 1 2", 
            "9 1 2 7 3 5 4 8 6",
            "8 4 5 6 1 2 9 7 3",
            "7 9 8 2 6 1 3 5 4",
            "5 2 6 4 7 3 8 9 1",
            "1 3 4 5 8 9 2 6 7",
            "4 6 9 1 2 8 7 3 5",
            "2 8 7 3 5 6 1 4 9",
            "3 5 1 9 4 7 6 2 8"]

print_board(board)

def most_constrained(board):
    constrained= empty_board(9)
    for row in range(9):
        for col in range(9):
            if (board[row][col] != 0):
                constrained[row][col] = 0
            else:
                constrained[row][col] = len(possible_values(board,row,col))
    return constrained

def possible_values(board,row,col):
    if (board[row][col] != 0):
        return set([board[row][col]])
    used_row = set([board[row][i] for i in range(9) if board[row][i] != 0])
    used_col = set([board[i][col] for i in range(9) if board[i][col] != 0])
    used_quad = set([board[r][c] for r,c in quadrant_coordinates(row,col) if board[r][c] != 0])
    #print("row:", row, "col:", col)
    #print("used_row:", used_row)
    #print("used_col:", used_col)
    #print("used_quad:", used_quad)
    used = used_row | used_col  | used_quad
    #print("used:", used)
    values = set( i for i in range(1,10) if i not in used )
    #print("possible values:", values)
    return values

def quadrant_coordinates(row,col):
    # input: row, col
    # output: list of [row, col] in the quadrant
    return [ [r + 3 * int(row / 3), c + 3 * int(col / 3)] for r in range(3) for c in range(3)]

print("---- constrained: ----")
print_board(most_constrained(board))

#print("---- sample of possible values: ----")
#for row in range(2):
#    for col in range(9):
#        print(row, col, "possible:", possible_values(board,row,col))



