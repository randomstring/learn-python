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

#possible_rows = [s for s in [[r+i for i in range(4)] for r in range(4)] if len(s) == 4]
#possible_cols = [s for s in [[r+i for i in range(4)] for r in range(3)] if len(s) == 4]
#all_possible = [[[(r,c) for r in rows] for c in cols] for rows in possible_rows for cols in possible_cols]
#print(all_possible)

# find_winner()
#   - given a board, if a player has won, return the player id (1 or 2)
#   - otherwise return 0
def find_winner(board):
    player = 0
    for r in range(6):
        for c in range(7):
            if board[r][c] != 0:
                player = board[r][c]
                # check for win in the col
                count = 1
                for ri in range(r+1,6):
                    if board[ri][c] == player:
                        count = count + 1
                    else:
                        break
                if count >= 4:
                    return player
                # check for win in the row
                count = 1
                for ci in range(c+1,7):
                    if board[r][ci] == player:
                        count = count + 1
                    else:
                        break
                if count >= 4:
                    return player
                # check diagonals
                count = 1
                for (ri,ci) in zip(range(r+1,6),range(c+1,7)):
                    if board[r][ci] == player:
                        count = count + 1
                    else:
                        break
                if count >= 4:
                    return player                                    
    return 0



# play
board = empty_board()
print_board(board)

# play a random game
while True:
    random_move(board,1)
    print_board(board)
    winner = find_winner(board)
    if winner != 0:
        print("the winner is player {0}".format(winner))
        break
    random_move(board,2)
    print_board(board)
    winner = find_winner(board)
    if winner != 0:
        print("the winner is player {0}".format(winner))
        break

if False:
    make_move(board,1,6)
    make_move(board,2,5)
    print_board(board)
    make_move(board,1,6)
    make_move(board,2,4)
    print_board(board)
    make_move(board,1,6)
    make_move(board,2,3)
    print_board(board)
    make_move(board,1,6)

    print_board(board)
    winner = find_winner(board)
    if winner != 0:
        print("the winner is player {0}".format(winner))
    print_board(board)

