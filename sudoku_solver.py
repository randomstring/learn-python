#!/usr/local/bin/python3

import sudoku
import argparse
import time

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
parser.add_argument('-b','--benchmark', action='store_true', help='time total amount of time for all puzzles')
parser.add_argument('-v','--verbose', action='store_true', help='more verbose output')
args = parser.parse_args()

start_time = time.time()
count = 0

# load game
puzzle_string = args.p
if args.verbose:
    print(puzzle_string)

game = sudoku.new_game(puzzle_string)
                  
# solve
sudoku.solve(game)

# print result
sudoku.print_game(game)

elapsed = time.time() - start_time
if args.verbose or args.benchmark:
    print('{0:.3f} seconds elapsed time for {1} puzzles in file {2}'.format(elapsed,count,''))
