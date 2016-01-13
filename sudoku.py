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
    #print_game(game)
    #print_possible(game)
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
        print('Solved It!')
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
    # XXX - todo
    # need to look for duplicates in row/col/quadrant
    # similar to possible_values, but need to find duplicates
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
            possible[r][col].add(val)
        else:
            possible[r][col].discard(val)
        # XXX only if board is not set
        if board[r][col] == 0:
            constrained[r][col] = len(possible[r][col])
        else:
            constrained[r][col] = 0
    for c in [x for x in range(9) if x != col]:
        if is_backtrack:
            possible[row][c].add(val)
        else:
            possible[row][c].discard(val)
        if board[row][c] == 0:
            constrained[row][c] = len(possible[row][c])
        else:
            constrained[row][c] = 0
    for r,c in [(r,c) for (r,c) in quadrant_coordinates(row,col) if r != row and c != col]:
        if is_backtrack:
            possible[r][c].add(val)
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
                print("DEAD END. Backtracking")
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
    print('Next Moves:',coords,'possible values:',possible_values)
    for val in list(possible_values):
        print('making move:',coords,'val:',val)
        make_moves(game,[[coords[0], coords[1], val]])
        game["tries"] += 1
        debug_game(game)
        solve(game)
        if (game["solved"] == True):
            break
        backtrack(game,[[coords[0], coords[1], val]])
        print('backtracking:',coords,'val:',val)
        debug_game(game)
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

    # From The Algorithm Design Manual 2nd Edition (S. S. Skiena) Page 239
    # this is a "hard" problem
    game = new_game()
    # .......12....35......6...7.7.....3.....4..8..1...........12.....8.....4..5....6..
    make_moves(game,[[0,7,1],[0,8,2],[1,4,3],[1,5,5],[2,3,6],[2,7,7],[3,0,7],[3,6,3],[4,3,4],[4,6,8],[5,0,1],[6,3,1],[6,4,2],[7,1,8],[7,7,4],[8,1,5],[8,6,6]])
    solve(game)
    solution = game["board"]

    # solution for reference
    if solution != [[6, 7, 3, 8, 9, 4, 5, 1, 2], 
                    [9, 1, 2, 7, 3, 5, 4, 8, 6],
                    [8, 4, 5, 6, 1, 2, 9, 7, 3],
                    [7, 9, 8, 2, 6, 1, 3, 5, 4],
                    [5, 2, 6, 4, 7, 3, 8, 9, 1],
                    [1, 3, 4, 5, 8, 9, 2, 6, 7],
                    [4, 6, 9, 1, 2, 8, 7, 3, 5],
                    [2, 8, 7, 3, 5, 6, 1, 4, 9],
                    [3, 5, 1, 9, 4, 7, 6, 2, 8]]:
        passed = False
        print("FAILED: test",test)
    else:
        print("PASSED: test",test)

    # Easy problem from American Airlines inflight Magazine
    test += 1
    game = new_game()
    #'..7.6....8.3...14292.8..5...5.2..9.42..584..13.4..1.2...5..6.18732...6.9....2.4..'
    make_moves(game,[[0,2,7],[0,4,6],[1,0,8],[1,2,3],[1,6,1],[1,7,4],[1,8,2],[2,0,9],[2,1,2],[2,3,8],[2,6,5],[3,1,5],[3,3,2],[3,6,9],[3,8,4],[4,0,2],[4,3,5],[4,4,8],[4,5,4],[4,8,1],[5,0,3],[5,2,4],[5,5,1],[5,7,2],[6,2,5],[6,5,6],[6,7,1],[6,8,8],[7,0,7],[7,1,3],[7,2,2],[7,6,6],[7,8,9],[8,4,2],[8,6,4]])
    solution = solve(game)
    if game["solved"] == True:
        print("PASSED: test",test)
    else:
        print("FAILED: test",test)
        passed = False

    # medium problem from American Airlines inflight Magazine
    test += 1
    game = new_game()
    #'..53..1.493.5..2.......6.5..5..28..1.94...82.8..61..7..6.1.......2..5.185.9..26..'
    make_moves(game,[[0,2,5],[0,3,3],[0,6,1],[0,8,4],[1,0,9],[1,1,3],[1,3,5],[1,6,2],[2,5,6],[2,7,5],[3,1,5],[3,4,2],[3,5,8],[3,8,1],[4,1,9],[4,2,4],[4,6,8],[4,7,2],[5,0,8],[5,3,6],[5,4,1],[5,7,7],[6,1,6],[6,3,1],[7,2,2],[7,5,5],[7,7,1],[7,8,8],[8,0,5],[8,2,9],[8,5,2],[8,6,6]])
    solution = solve(game)
    if game["solved"] == True:
        print("PASSED: test",test)
    else:
        print("FAILED: test",test)
        passed = False

    # hard problem from American Airlines inflight Magazine
    test += 1
    game = new_game()
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
    solution = solve(game)
    if game["solved"] == True:
        print("PASSED: test",test)
    else:
        print("FAILED: test",test)
        passed = False

    # Norvig's hardest sudoku problem http://norvig.com/sudoku.html  (takes 0.09 s)
    test += 1
    game = new_game()
    make_moves(game,move_list_from_strings(['.....6....59.....82....8....45........3........6..3.54...325..6..................']))
    solution = solve(game)
    if game["solved"] == True:
        print("PASSED: test",test)
    else:
        print("FAILED: test",test)
        passed = False
    
    puzzles = [
        '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......',
        '52...6.........7.13...........4..8..6......5...........418.........3..2...87.....',
        '6.....8.3.4.7.................5.4.7.3..2.....1.6.......2.....5.....8.6......1....',
        ]
    solutions = [
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

