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
