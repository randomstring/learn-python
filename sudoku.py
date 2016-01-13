#!/usr/bin/python3
#
# Sudoku Solver
#
import time

# create new game board
def empty_board(size): return [ [ 0 for i in range(size)] for i in range(size)]

# create new game data structure
def new_game(puzzle=None):
    game = {"filled": 0, "board": empty_board(9), "solved": False, "tries": 0 }
    # init possible and constrained
    game["possible"] = new_possible_board(game)
    game["constrained"] = new_constrained_board(game)
    if puzzle:
        make_moves(game,move_list_from_strings([puzzle]))
    # print_game(game)
    # print_possible(game)
    # print_board(game["constrained"])
    return game

# return elapsed time for solving puzzle
def elapsed(game):
    if not game["start_time"]:
        return 0
    if game["end_time"]:
        return game["end_time"] - game["start_time"]
    return time.time() - game["start_time"]

def debug_game(game):
    print_game(game)
    print_possible(game)
    print('----------------------------------')

# print the sudoku game: board, salved state, elapsed time to solve
def print_game(game):
    print_board(game["board"])
    if (game["solved"] == True):
        elapsed = game["end_time"] - game["start_time"]
        print("Solved! in", game["tries"], "tries and", elapsed, "seconds")
    else:
        print("filled in so far:", game["filled"])

# print the sudoku board
def print_board(board):
    for (i,row) in enumerate(board):
        #print("row", i, ":",end="")
        for val in row:
            if val == 0:
                print(" . ",end="")
            else:
                print(" ",val," ",end="",sep="")
        print("")

# return the current puzzle state as a string
def puzzle_entry(x):
    if x == 0:
        return '.'
    return str(x)

def board_string(board):
    return ''.join([''.join([puzzle_entry(x) for x in row]) for row in board])

def puzzle_string(game):
    return board_string(game["board"])

def print_possible(game):
    board = game["board"]
    possible = game["possible"]
    expanded = [[" " for c in range(27)] for r in range(27)]
    for (i,row) in enumerate(possible):
        for (j, col) in enumerate(row):
            p = list(col)
            if board[i][j] != 0:
                p = [ board[i][j] ]
            for k in p:
                expanded[i*3 + int((k-1)/3)][j*3 + ((k-1)%3)] = str(k)
    for (i,row) in enumerate(expanded):
        if i % 3 == 0:
            print('---+---+---+---+---+---+---+---+---')
        # GAGK - fix me
        row.insert(24,'|')
        row.insert(21,'|')
        row.insert(18,'|')
        row.insert(15,'|')
        row.insert(12,'|')
        row.insert(9,'|')
        row.insert(6,'|')
        row.insert(3,'|')
        print(''.join(row))

def make_moves(game, moves):
    # make a list of moves
    # moves is a list [ x, y, value ]
    for move in moves:
        [x, y, val] = move
        if game["board"][x][y] == 0:
            game["filled"] += 1
        else:
            print("making a move on a coordinate that is already filled in:", x, y, val)
        game["board"][x][y] = val
        update_possible_board(game,x,y,val,False)
    if game["filled"] == 81:
        game["solved"] = True

def backtrack(game, moves):
    # undo a list of moves
    # moves is a list [ x, y, value ]
    for move in moves:
        [x, y, val] = move
        if game["board"][x][y] != 0:
            game["filled"] -= 1
        else:
            print("backtracking on an empty coordinate:", x, y)
        game["board"][x][y] = 0
        update_possible_board(game,x,y,val,True)
    if game["filled"] < 0:
        print("oh no, we have negative moves")

# Create a board (matrix) with a count of how many possible values can
# legally satisfy that square. We use this to pick which square to
# fill in next.
def most_constrained(board):
    constrained= empty_board(9)
    for row in range(9):
        for col in range(9):
            if (board[row][col] != 0):
                constrained[row][col] = 0
            else:
                constrained[row][col] = len(possible_values(board,row,col))
    return constrained

# check if puzzle is solvable
def is_solvable(game):
    # Thought about this. Have to try to solve and see if we can. Need to add
    # check to see if we failed or not.
    pass

def is_valid_solution(game):
    # TODO
    # double check to see if this is a valid solution
    pass

# Given a game board and a row, col determine all the legal values
# that can fill in that square. Used to create a list of values to try
# for that square.
def possible_values(board,row,col):
    if row >= 9 or col >= 9:
        return set()
    if (board[row][col] != 0):
        return set([board[row][col]])
    used_row = set([board[row][i] for i in range(9) if board[row][i] != 0])
    used_col = set([board[i][col] for i in range(9) if board[i][col] != 0])
    used_quad = set([board[r][c] for r,c in quadrant_coordinates(row,col) if board[r][c] != 0])
    used = used_row | used_col | used_quad
    values = set( i for i in range(1,10) if i not in used )
    return values

# update the possible move board given a move, or move backtrack
def update_possible_board(game,row,col,val,is_backtrack):
    board = game["board"]
    possible = game["possible"]
    constrained = game["constrained"]
    for r in range(9):
        if is_backtrack:
            possible[r][col] = possible_values(board,r,col)
        else:
            possible[r][col].discard(val)
        if board[r][col] == 0:
            constrained[r][col] = len(possible[r][col])
        else:
            constrained[r][col] = 0
    for c in [x for x in range(9) if x != col]:
        if is_backtrack:
            possible[row][c] = possible_values(board,row,c)
        else:
            possible[row][c].discard(val)
        if board[row][c] == 0:
            constrained[row][c] = len(possible[row][c])
        else:
            constrained[row][c] = 0
    for r,c in [(r,c) for (r,c) in quadrant_coordinates(row,col) if r != row and c != col]:
        if is_backtrack:
            possible[r][c] = possible_values(board,r,c)
        else:
            possible[r][c].discard(val)
        if board[r][c] == 0:
            constrained[r][c] = len(possible[r][c])
        else:
            constrained[r][c] = 0
    # game["possible"] = possible
    # game["constrained"] = constrained

def new_possible_board(game):
    return [ [ set(range(1,10)) for col in range(9)] for row in range(9)]

def new_constrained_board(game):
    return [ [ 9 for col in range(9)] for row in range(9)]

def gen_possible(game):
    return [ [ possible_values(game["board"],row,col) for col in range(9)] for row in range(9)]

def gen_constrained(game):
    return [ [ len(game["possible"][row][col]) for col in range(9)] for row in range(9)]

def possible_values_fast(game,row,col):
    return game["possible"][row][col]

# return the list of coordinates for the quadrant that the given row,
# col square is located.
def quadrant_coordinates(row,col):
    # input: row, col
    # output: list of [row, col] in the quadrant
    return [ [r + 3 * int(row / 3), c + 3 * int(col / 3)] for r in range(3) for c in range(3)]

def most_constrained_move(game):
    # for a given game state return [row, col, (set of possible
    # values)] for the most constrained possition of the game
    constrained = game["constrained"]
    min = 10
    coords = [9,9]
    for row in range(9):
        for col in range(9):
            if constrained[row][col] == 0 and game["board"][row][col] == 0:
                # dead end, we have a coordinate with no valid values
                # print("DEAD END. Backtracking")
                return [ [9,9], set() ]
            #if constrained[row][col] != 0 and constrained[row][col] < min:
            if constrained[row][col] != 0 and constrained[row][col] < min and game["board"][row][col] == 0:
                min = constrained[row][col]
                coords = [row, col]
    return [ coords, game["possible"][coords[0]][coords[1]] ]

def solve(game):
    # 1. pick most constrained coordinate and try all legal values
    # 2. recersively solve the rest of the puzzle
    if "start_time" not in game:
        game["start_time"] = time.time()
    if game["solved"] == True:
        return
    [coords, possible_values] = most_constrained_move(game)
    # print('Next Moves:',coords,'possible values:',possible_values)
    for val in list(possible_values):
        # print('making move:',coords,'val:',val)
        make_moves(game,[[coords[0], coords[1], val]])
        game["tries"] += 1
        # debug_game(game)
        solve(game)
        if (game["solved"] == True):
            break
        backtrack(game,[[coords[0], coords[1], val]])
        # print('backtracking:',coords,'val:',val)
        # debug_game(game)
    if game["solved"] == True and "end_time" not in game:
        game["end_time"] = time.time()

# Set board directly from puzzle string, bypass make_moves()
def set_puzzle(game,puzzle_string):
    for i,val in enumerate(puzzle_string):
        if val == '.':
            val = 0
        else:
            game["filled"] += 1
        game["board"][int(i / 9)][i % 9] = int(val)

# Generate a list of moves given either 1) an array of row strings or
# 2) one long string with all the filled in squares
def move_list_from_strings(lines):
    moves = []
    if len(lines) == 1:
        # format: one list of elements "...2...5...1" or "10004000700" etc.
        for i,val in enumerate(lines[0]):
            if val != '.' and val != '0':
                moves.append([int(i / 9), i % 9, int(val)])
    else:
        # format: list of rows
        for row,line in enumerate(lines):
            for col, val in enumerate(line.split()):
                if val != '.' and val != '0':
                    moves.append([row,col,int(val)])
    return moves

def test():
    passed = True
    test = 1
    puzzles = [
        # From The Algorithm Design Manual 2nd Edition (S. S. Skiena) Page 239
        '.......12....35......6...7.7.....3.....4..8..1...........12.....8.....4..5....6..',
        # Easy problem from American Airlines inflight Magazine
        '..7.6....8.3...14292.8..5...5.2..9.42..584..13.4..1.2...5..6.18732...6.9....2.4..',
        # medium problem from American Airlines inflight Magazine
        '..53..1.493.5..2.......6.5..5..28..1.94...82.8..61..7..6.1.......2..5.185.9..26..',
        # hard problem from American Airlines inflight Magazine
        '37.4..1.........2....2.1.53.....96144...2...77693.....92.1.6....1.........8..2.91',
        # Norvig's hardest sudoku problem http://norvig.com/sudoku.html  (takes 0.09 s)
        #'.....6....59.....82....8....45........3........6..3.54...325..6..................', #orig
        '.....6....59.....82....8....45........3........6..3.54...325..6..............1283', # make it easier
        # from top95.txt
        '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......',
        '52...6.........7.13...........4..8..6......5...........418.........3..2...87.....',
        '6.....8.3.4.7.................5.4.7.3..2.....1.6.......2.....5.....8.6......1....',
        ]
    solutions = [
        '673894512912735486845612973798261354526473891134589267469128735287356149351947628',
        '547162893863759142921843576156237984279584361384691725495376218732418659618925437',
        '285397164936541287471286359657428931194753826823619475768134592342965718519872643',
        '372458169156937428894261753235789614481625937769314582923146875517893246648572391',
        '834296715659174328271538469945862137183457692726913854418325976362789541597641283',
        '417369825632158947958724316825437169791586432346912758289643571573291684164875293',
        '527316489896542731314987562172453896689271354453698217941825673765134928238769145',
        '617459823248736915539128467982564371374291586156873294823647159791385642465912738',
        ]

    for (p,s) in zip(puzzles,solutions):
        test += 1
        game = new_game(p)
        solution = solve(game)
        if puzzle_string(game) == s:
            print("PASSED: test",test)
        else:
            print("FAILED: test",test)
            passed = False

    return passed

