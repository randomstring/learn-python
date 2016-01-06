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
group = parser.add_mutually_exclusive_group()
group.add_argument('-p', metavar='puzzle', help='sudoku puzzle string')
group.add_argument('-f', metavar='filename', help='filename containing puzzle string(s)')

args = parser.parse_args()

# load game
puzzle_string = args.puzzle
print(puzzle_string)

game = sudoku.new_game()
moves = sudoku.move_list_from_strings([puzzle_string])
sudoku.make_moves(game,moves)
                  
# solve
sudoku.solve(game)

# print result
sudoku.print_game(game)
