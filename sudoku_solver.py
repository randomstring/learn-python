#!/usr/local/bin/python3

import sudoku
import argparse
import time
import sys

# parse arguments
parser = argparse.ArgumentParser(description='Solve a Sudoku puzzle.',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog= '''
Example puzzle format:
...............9..97.3......1..6.5....47.8..2.....2..6.31..4......8..167.87......
'''
)

group = parser.add_mutually_exclusive_group()
group.add_argument('-p', metavar='puzzle', help='sudoku puzzle string')
group.add_argument('-f', metavar='filename',
                   type=argparse.FileType('r'),
                   help='filename containing puzzle string(s)')
parser.add_argument('-b','--benchmark', action='store_true', help='time total amount of time for all puzzles')
parser.add_argument('-t','--test', action='store_true', help='run regression tests')
parser.add_argument('-c','--deepcopy', action='store_true', help='use deep copy for backtracking')
parser.add_argument('-v','--verbose', action='store_true', help='more verbose output')
args = parser.parse_args()

if args.test:
    sudoku.test(args.deepcopy)
    quit()

start_time = time.time()
count = 0

# Todo: generate histogram for benchmarked completion times
hist = {}

# load game
puzzles = []
if args.p != None:
    puzzles.append(args.p)
else:
    # read in a list of puzzles from a file or default to standard in
    input = args.f
    if input is None:
        if args.verbose:
            print('Reading puzzle(s) from stdin.');
        input = sys.stdin
    elif args.verbose:
        print('Reading puzzles from file [{0}]'.format(input.name))
    for puzzle in input:
        puzzles.append(puzzle.rstrip())

for puzzle in puzzles:
    count += 1
    if args.verbose:
        print(puzzle)
    game = sudoku.new_game(puzzle)
    if args.deepcopy:
        print("using deepcopy")
        sudoku.deepcopy(game,True)
    sudoku.solve(game)
    if args.benchmark:
        print(sudoku.puzzle_string(game),"{:7.3f}".format(sudoku.elapsed(game)))
    else:
        sudoku.print_game(game)

elapsed = time.time() - start_time
if args.verbose or args.benchmark:
    print('{0:.3f} seconds elapsed time for {1} puzzles in file {2}'.format(elapsed,count,''))
