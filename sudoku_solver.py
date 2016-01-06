#!/usr/local/bin/python3

import sudoku
import argparse

# parse arguments
parser = argparse.ArgumentParser(description='Solve a Sudoku puzzle.',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog= '''
Example puzzle format:
.....6....59.....82....8....45........3........6..3.54...325..6..................
'''
                                 )

parser.add_argument('puzzle', metavar='P', help='sudoku puzzle string')
args = parser.parse_args()

game = sudoku.new_game()
# load game
puzzle_string = args.puzzle
print(puzzle_string)

moves = sudoku.move_list_from_strings([puzzle_string])
sudoku.make_moves(game,moves)
                  
# solve
sudoku.solve(game)

# print result
sudoku.print_game(game)
