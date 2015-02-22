#!/usr/bin/python3
#
# Sudoku Solver
#

def print_game(game):
    print_board(game["board"])
    if (game["solved"] == True):
        print("Solved! in", game["tries"], "tries")
    else:
        print("filled in so far:", game["filled"])

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

def make_moves(game, moves):
    # make a list of moves
    # moves is a list [ x, y, value ]
    for move in moves:
        [x, y, val] = move
        if game["board"][x][y] == 0:
            game["filled"] = game["filled"] + 1
        else:
            print("making a move on a coordinate that is already filled in:", x, y, val)
        game["board"][x][y] = val
    if game["filled"] == 81:
        game["solved"] = True

def backtrack(game, moves):
    # undo a list of moves
    # moves is a list [ x, y, value ]
    for move in moves:
        [x, y] = move
        if game["board"][x][y] != 0:
            game["filled"] = game["filled"] - 1
        else:
            print("backtracking on an empty coordinate:", x, y)
        game["board"][x][y] = 0
    if game["filled"] < 0:
        print("oh no, we have negative moves")


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
    if row >= 9 or col >= 9:
        return set()
    if (board[row][col] != 0):
        return set([board[row][col]])
    used_row = set([board[row][i] for i in range(9) if board[row][i] != 0])
    used_col = set([board[i][col] for i in range(9) if board[i][col] != 0])
    used_quad = set([board[r][c] for r,c in quadrant_coordinates(row,col) if board[r][c] != 0])
    used = used_row | used_col  | used_quad
    values = set( i for i in range(1,10) if i not in used )
    return values

def quadrant_coordinates(row,col):
    # input: row, col
    # output: list of [row, col] in the quadrant
    return [ [r + 3 * int(row / 3), c + 3 * int(col / 3)] for r in range(3) for c in range(3)]

def most_constrained_move(game):
    # for a given game state return [row, col, (set of possible
    # values)] for the most constrained possition of the game
    constrained = most_constrained(game["board"])
    min = 10
    coords = [9,9]
    for row in range(9):
        for col in range(9):
            if constrained[row][col] == 0 and game["board"][row][col] == 0:
                # dead end, we have a coordinate with no valid values
                return [ [9,9], set() ]
            if constrained[row][col] != 0 and constrained[row][col] < min:
                min = constrained[row][col]
                coords = [row, col]
    return [ coords, possible_values(game["board"], coords[0], coords[1])]

def solve_sudoku(game):
    # 1. pick most constrained coordinate and try all legal values
    # 2. recersively solve the rest of the puzzle
    if game["solved"] == True:
        return
    [coords, possible_values] = most_constrained_move(game)
    # print("next move is coords:", coords, "possible values:", possible_values)
    for val in list(possible_values):
        make_moves(game,[[coords[0], coords[1], val]])
        game["tries"] += 1
        # print_game(game)
        solve_sudoku(game)
        if (game["solved"] == True):
            break
        backtrack(game,[[coords[0], coords[1]]])

def move_list_from_strings(lines):
    moves = []
    for row,line in enumerate(lines):
        for col, val in enumerate(line.split()):
            if val != '.':
                moves.append([row,col,int(val)])
    return moves

#
# Set up Game board
#
game = {"filled": 0, "board": empty_board(9), "solved": False, "tries": 0 }

# choose problem 1-4
game_number = 4

if game_number == 1:
    # From The Algorithm Design Manual 2nd Edition (S. S. Skiena) Page 239
    # this is a "hard" problem
    make_moves(game,[[0,7,1],[0,8,2],[1,4,3],[1,5,5],[2,3,6],[2,7,7],[3,0,7],[3,6,3],[4,3,4],[4,6,8],[5,0,1],[6,3,1],[6,4,2],[7,1,8],[7,7,4],[8,1,5],[8,6,6]])
    
    # Some Hints (to make it faster for testing)
    make_moves(game,[[0,0,6],[0,1,7],[0,2,3],[1,0,9],[2,0,8]])   # about 0.11 s
    # make_moves(game,[[0,0,6],[0,1,7]])                           # about 0.25 s
    # make_moves(game,[[0,0,6]])                                   # about 10 s
    # with no hints it takes about 20 s

    # solution for reference
    solution = ["6 7 3 8 9 4 5 1 2", 
                "9 1 2 7 3 5 4 8 6",
                "8 4 5 6 1 2 9 7 3",
                "7 9 8 2 6 1 3 5 4",
                "5 2 6 4 7 3 8 9 1",
                "1 3 4 5 8 9 2 6 7",
                "4 6 9 1 2 8 7 3 5",
                "2 8 7 3 5 6 1 4 9",
                "3 5 1 9 4 7 6 2 8"]
elif game_number == 2:
    # Easy problem from American Airlines inflight Magazine
    make_moves(game,[[0,2,7],[0,4,6],[1,0,8],[1,2,3],[1,6,1],[1,7,4],[1,8,2],[2,0,9],[2,1,2],[2,3,8],[2,6,5],[3,1,5],[3,3,2],[3,6,9],[3,8,4],[4,0,2],[4,3,5],[4,4,8],[4,5,4],[4,8,1],[5,0,3],[5,2,4],[5,5,1],[5,7,2],[6,2,5],[6,5,6],[6,7,1],[6,8,8],[7,0,7],[7,1,3],[7,2,2],[7,6,6],[7,8,9],[8,4,2],[8,6,4]])
elif game_number == 3:
    # medium problem from American Airlines inflight Magazine
    make_moves(game,[[0,2,5],[0,3,3],[0,6,1],[0,8,4],[1,0,9],[1,1,3],[1,3,5],[1,6,2],[2,5,6],[2,7,5],[3,1,5],[3,4,2],[3,5,8],[3,8,1],[4,1,9],[4,2,4],[4,6,8],[4,7,2],[5,0,8],[5,3,6],[5,4,1],[5,7,7],[6,1,6],[6,3,1],[7,2,2],[7,5,5],[7,7,1],[7,8,8],[8,0,5],[8,2,9],[8,5,2],[8,6,6]])
else:
    # hard problem from American Airlines inflight Magazine
    problem4 = ["3 7 . 4 . . 1 . .",
                ". . . . . . . 2 .",
                ". . . 2 . 1 . 5 3",
                ". . . . . 9 6 1 4",
                "4 . . . 2 . . . 7",
                "7 6 9 3 . . . . .",
                "9 2 . 1 . 6 . . .",
                ". 1 . . . . . . .",
                ". . 8 . . 2 . 9 1"]
    make_moves(game,move_list_from_strings(problem4))

#
# Solve the puzzle
#
print("--- starting possition", game_number, "---")
print_game(game)
solve_sudoku(game)
print("--- final possition ---")
print_game(game)


