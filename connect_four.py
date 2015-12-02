#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#!/Users/dole/anaconda/bin/python3
#
# Connect Four
#
import random

def empty_board(): return [ [ 0 for i in range(7)] for i in range(6)] 

player_tokens = ['.', 'X', 'O']

def print_board(board):
    for (i,row) in reversed(list(enumerate(board))):
        print("row", (i+1), ":",end="")
        for val in row:
            print(" ",player_tokens[val]," ",end="",sep="")
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

def backtrack(board,column):
    for row in reversed(range(6)):
        if board[row][column] != 0:
            board[row][column] = 0
            return
    assert False, print('tried to backtrack on empty column {0}',format(column))

def legal_moves(board):
    return [col for col in range(7) if board[5][col] == 0]

def random_move(board,player):
    moves = legal_moves(board)
    if len(moves) > 0:
        random.shuffle(moves)
        make_move(board,player,moves[0])
        return
    assert False, print('no more legal moves')

def better_than_random_move(board,player):
    moves = legal_moves(board)
    if len(moves) > 0:
        for c in moves:
            make_move(board,player,c)
            if find_winner(board) == player:
                return
            backtrack(board,c)
        # otherwise make a random move
        random_move(board,player)
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
                    if board[ri][ci] == player:
                        count = count + 1
                    else:
                        break
                if count >= 4:
                    return player                                    
                count = 1
                for (ri,ci) in zip(range(r+1,6),reversed(range(0,c))):
                    if board[ri][ci] == player:
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
while False:
    random_move(board,1)
    print_board(board)
    winner = find_winner(board)
    if winner != 0:
        print("the winner is player {0}".format(player_tokens[winner]))
        break
    random_move(board,2)
    print_board(board)
    winner = find_winner(board)
    if winner != 0:
        print("the winner is player {0}".format(player_tokens[winner]))
        break

count = 0
while True:
    player = (count % 2) + 1
    better_than_random_move(board,player)
    print_board(board)
    winner = find_winner(board)
    if winner != 0:
        print("the winner is player {0}".format(player_tokens[winner]))
        break
    count = count + 1

if False:
    board = empty_board()
    print_board(board)
    # Test column win
    make_move(board,1,6)
    make_move(board,2,5)
    make_move(board,1,6)
    make_move(board,2,4)
    make_move(board,1,6)
    make_move(board,2,3)
    make_move(board,1,6)
    print_board(board)
    winner = find_winner(board)
    if winner != 0:
        print("the winner is player {0}".format(player_tokens[winner]))

if False:
    # Test back diag win
    board = empty_board()
    print_board(board)
    make_move(board,2,5)
    make_move(board,2,4)
    make_move(board,2,4)
    make_move(board,2,3)
    make_move(board,2,3)
    make_move(board,2,3)
    make_move(board,1,6)
    make_move(board,1,5)
    make_move(board,1,4)
    make_move(board,1,3)
    print_board(board)
    winner = find_winner(board)
    if winner != 0:
        print("the winner is player {0}".format(player_tokens[winner]))

if False:
    # Test back diag win
    board = empty_board()
    print_board(board)
    make_move(board,2,5)
    make_move(board,2,5)
    make_move(board,2,5)
    make_move(board,2,4)
    make_move(board,2,4)
    make_move(board,2,3)
    make_move(board,1,2)
    make_move(board,1,3)
    make_move(board,1,4)
    make_move(board,1,5)
    print_board(board)
    winner = find_winner(board)
    if winner != 0:
        print("the winner is player {0}".format(player_tokens[winner]))

