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

### Debug Output

So when I rewrote this to be faster, I introduced a bug and then ended
up writing some fun routines to debug the puzzle state. For instance
you can dump all the possible values given the puzzle's current setup.

```python
import sudoku
puzzle='..42.....8.....3..39......5..8.91....2...65...3......6.1....98....4.37.....5.....'
game = sudoku.new_game(puzzle)
sudoku.print_possible(game)
```

outputs:
```
---+---+---+---+---+---+---+---+---
1  |   |   | 2 |1 3|   |1  |1  |1  
 56| 56|4  |   | 56| 5 |  6|  6|   
7  |7  |   |   |78 |789| 8 |7 9|789
---+---+---+---+---+---+---+---+---
   |   |12 |1  |1  |   |  3|12 |12 
   | 56| 56|  6|456|45 |   |4 6|4  
 8 |7  |7  |7 9|7  |7 9|   |7 9|7 9
---+---+---+---+---+---+---+---+---
  3|   |12 |1  |1  |   |12 |12 |   
   |   |  6|  6|4 6|4  |4 6|4 6| 5 
   |  9|7  |78 |78 |78 | 8 |7  |   
---+---+---+---+---+---+---+---+---
   |   |   |  3|   |1  | 2 | 23| 23
456|456|   |   |   |   |4  |4  |4  
7  |7  | 8 |7  |  9|   |   |7  |7  
---+---+---+---+---+---+---+---+---
1  | 2 |1  |  3|  3|   |   |1 3|1 3
4  |   |   |   |4  |  6| 5 |4  |4  
7 9|   |7 9|78 |78 |   |   |7 9|789
---+---+---+---+---+---+---+---+---
1  |  3|1  |   | 2 | 2 |12 |12 |   
45 |   | 5 |   |45 |45 |4  |4  |  6
7 9|   |7 9|78 |78 |78 | 8 |7 9|   
---+---+---+---+---+---+---+---+---
 2 |1  | 23|   | 2 | 2 |   |   | 23
456|   | 56|  6|  6|   |   |   |4  
7  |   |7  |7  |7  |7  |  9| 8 |   
---+---+---+---+---+---+---+---+---
 2 |   | 2 |   |12 |  3|   |12 |12 
 56| 56| 56|4  |  6|   |   | 56|   
  9| 8 |  9|   | 8 |   |7  |   |   
---+---+---+---+---+---+---+---+---
 2 |   | 23|   |12 | 2 |12 |123|123
4 6|4 6|  6| 5 |  6|   |4 6|4 6|4  
7 9|78 |7 9|   |78 |789|   |   |   
```


## Connect Four

Play a game of connect four. Use alpha-beta pruning to pick computer's move.


## Misc. Programming Practice

Dynamic programming, implementing qsort, etc.
