# learn-python

Various practice problems to help learn Python.

# Sudoku Solver

Python module to solve Sudoku puzzles.

'''python
import sudoku
puzzle='........4.7..91...96..2.....16..7...4..93.....3.8...2.3......1.....7...8.....8.35'
game = sudoku.new_game(puzzle)
sudoku.solve(game)
sudoku.print_game(game)

'''