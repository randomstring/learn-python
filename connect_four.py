#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#!/Users/dole/anaconda/bin/python3
#
# Connect Four
#
import random

def empty_board(): return [ [ 0 for i in range(7)] for i in range(6)] 

def print_board(board):
    for (i,row) in reversed(list(enumerate(board))):
        print("row", (i+1), ":",end="")
        for val in row:
            if val == 0:
                print(" . ",end="")
            else:
                piece = "O"
                if val == 1:
                    piece = "X"
                print(" ",piece," ",end="",sep="")
        print("")
    print("----------------------------")
    print("column:",end="")
    for i in range(7):
        print(" ",i+1," ",end="",sep="")
    print("")


def make_move(board,player,column):
    assert player >= 1 and player <= 2, "bad player value: %r" % player
    assert column >= 0 and column <= 6, "bad column value: %r" % column
    for row in range(6):
        if board[row][column] == 0:
            board[row][column] = player
            return
    assert False, print('illegal move by player {0} in column {1}'.format(player,column))

def legal_moves(board):
    return [col for col in range(7) if board[5][col] == 0]

def random_move(board,player):
    moves = legal_moves(board)
    if len(moves) > 0:
        random.shuffle(moves)
        make_move(board,player,moves[0])
        return
    assert False, print('no more legal moves')

def in_bounds(row,col):
    """
    >>> in_bounds(0,0)
    True
    >>> in_bounds(5,6)
    True
    >>> in_bounds(-1,0)
    False
    >>> in_bounds(6,6)
    False
    >>> in_bounds(5,7)
    False
    """
    return row >= 0 and row < 6 and col >= 0 and col < 7

possible_rows = [s for s in [[r+i for i in range(4)] for r in range(4)] if len(s) == 4]
possible_cols = [s for s in [[r+i for i in range(4)] for r in range(3)] if len(s) == 4]

all_possible = [[[(r,c) for r in rows] for c in cols] for rows in possible_rows for cols in possible_cols]
print(all_possible)

# return all possible connect four coordinate sequences for a given coord
def possible_connect_fours(row,col):
    possibilities = []
    # find possible rows an columns that contain the coordinate
    # generate all possible connect fours
    return possibilities


# find_winner()
#   - given a board, if a player has won, return the player id (1 or 2)
#   - otherwise return 0
def find_winner(board):
    return 0

# play
board = empty_board()
print_board(board)

# play a random game
while False:
    random_move(board,1)
    random_move(board,2)
    print_board(board)

print(possible_connect_fours(0,0))
print(possible_connect_fours(0,3))
