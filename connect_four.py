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

# play
board = empty_board()
print_board(board)

# play a random game
while True:
    random_move(board,1)
    random_move(board,2)
    print_board(board)
