# Learning Python

Various practice problems to help learn Python.

## Sudoku Solver

Python module to solve Sudoku puzzles.

```python
import sudoku
puzzle='........4.7..91...96..2.....16..7...4..93.....3.8...2.3......1.....7...8.....8.35'
game = sudoku.new_game(puzzle)
sudoku.solve(game)
# print solution as a string
print(sudoku.puzzle_string(game))
# print solution as 9x9 game board
sudoku.print_game(game)
```
outputs:
```
125683974874591362963724581216457893487932156539816427348265719651379248792148635
 1  2  5  6  8  3  9  7  4 
 8  7  4  5  9  1  3  6  2 
 9  6  3  7  2  4  5  8  1 
 2  1  6  4  5  7  8  9  3 
 4  8  7  9  3  2  1  5  6 
 5  3  9  8  1  6  4  2  7 
 3  4  8  2  6  5  7  1  9 
 6  5  1  3  7  9  2  4  8 
 7  9  2  1  4  8  6  3  5 
Solved! in 1058 tries and 0.124 seconds
```

## Connect Four

Play a game of connect four. Use alpha-beta pruning to pick computer's move.


## Misc. Programming Practice

Dynamic programming, implementing qsort, etc.