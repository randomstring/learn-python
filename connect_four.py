#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#!/Users/dole/anaconda/bin/python3
#
# Connect Four
#
import random
from operator import itemgetter

def empty_board(): return [ [ 0 for i in range(7)] for i in range(6)] 

player_tokens = ['.', 'X', 'O']

board_scores = {}

def board_key(board):
    return ''.join(str(board[r][c]) for r in range(6) for c in range(7))

def print_board(board):
    for (i,row) in reversed(list(enumerate(board))):
        print("row", i, ":",end="")
        for val in row:
            print(" ",player_tokens[val]," ",end="",sep="")
        print("")
    print("----------------------------")
    print("column:",end="")
    for i in range(7):
        print(" ",i," ",end="",sep="")
    print("")

def next_player(player):
    if player == 1:
        return 2
    return 1

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

def score(board,player,depth):
    winner = find_winner(board)
    if winner == 1:
        return 1
    elif winner != 0:
        return -1
    key = board_key(board)
    # recurse
    if depth <= 0:
        return 0
    moves = legal_moves(board)
    if len(moves) == 0:
        # tie
        return 0
    next = next_player(player)
    scores = []
    for move in moves:
        score = move_score(board,next,move,depth-1)
        scores.append((move,score))
        if next == 1 and score == 1:
            break
        if next == 2 and score == -1:
            break
    # scores = {(move,move_score (board,next,move,depth-1)) for move in moves}
    # print(next,scores)
    if next == 1:
        score = max([score for (move,score) in scores])
    else:
        score = min([score for (move,score) in scores])
    return score

def estimated_move_score(board,player,move):
    make_move(board,player,move)
    s = estimated_score(board)
    backtrack(board,move)
    return s

def move_score(board,player,move,depth):
    make_move(board,player,move)
    s = score(board,player,depth)
    backtrack(board,move)
    return s

max_depth = 4
def best_move(board,player):
    if board[0][3] == 0:
        # special case for best first move
        make_move(board,player,3)
        return
    moves = legal_moves(board)
    if (len(moves) > 0):
        estimated_scores = {(move,estimated_move_score(board,player,move)) for move in moves}
        reverse = False
        if player == 1:
            reverse = True
        sorted(estimated_scores, key=itemgetter(1), reverse=reverse) 
        print('best_move: player {0} {1}'.format(player,estimated_scores))

        best = (-1,0)
        for (move,est_score) in estimated_scores:
            score = move_score(board,player,move,max_depth)
            
            if best[0] == -1:
                best = (move,score)

            if player == 1:
                if score == 1:
                    best = (move,score)
                    break
                elif score > best[1]:
                    best = (move,score)
                elif score < best[1]:
                    break
            else:
                if score == -1:
                    best = (move,score)
                    break
                elif score < best[1]:
                    best = (move,score)
                elif score > best[1]:
                    break

        make_move(board,player,best[0])
        print('best_move: player {0} is {1} score {2}'.format(player,best[0],best[1]))
        return
    print_board(board)
    assert False, print('no more legal moves')

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

def score_delta(player,count,blocked):
    score = 0
    if count >= 4:
        if player == 1:
            return 100
        else:
            return -100
    if blocked != 0:
        return 0
    if count == 3:
        score = 0.01
    elif count == 2:
        score = 0.0001
    if player == 1:
        return score
    else:
        return -score


# score position by creating an estimate of how many win posibilities
#   Given a board
#   a) return 1 if player 1 won
#   b) return -1 if player 2 won
#   c) otherwise return a heuristic score of who's winning
def estimated_score(board):
    player = 0
    score = 0
    for r in range(6):
        for c in range(7):
            if board[r][c] != 0:
                player = board[r][c]
                opponent = next_player(player)
                # check for win in the col
                count = 1
                blocked = 0
                for ri in range(r+1,6):
                    if board[ri][c] == player:
                        count = count + 1
                    elif board[ri][c] == opponent:
                        blocked = 1
                score += score_delta(player,count,blocked)

                # check for win in the row
                count = 1
                blocked = 0
                for ci in range(c+1,7):
                    if board[r][ci] == player:
                        count = count + 1
                    elif board[r][ci] == opponent:
                        blocked = 1
                score += score_delta(player,count,blocked)

                # check diagonals
                count = 1
                blocked = 0
                for (ri,ci) in zip(range(r+1,6),range(c+1,7)):
                    if board[ri][ci] == player:
                        count = count + 1
                    elif board[ri][ci] == opponent:
                        blocked = 1
                score += score_delta(player,count,blocked)

                count = 1
                blocked = 0
                for (ri,ci) in zip(range(r+1,6),reversed(range(0,c))):
                    if board[ri][ci] == player:
                        count = count + 1
                    elif board[ri][ci] == opponent:
                        blocked == 1

                score += score_delta(player,count,blocked)
    return score

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

# play random vs. better than random
count = 0
while False:
    player = (count % 2) + 1
    better_than_random_move(board,player)
    print_board(board)
    winner = find_winner(board)
    if winner != 0:
        print("the winner is player {0}".format(player_tokens[winner]))
        break
    count = count + 1

def computer_vs_computer():
    # play Computer vs Computer
    player = 1
    board = empty_board()
    moves = 0
    while True:
        if player == 1:
            best_move(board,player)
        else:
            best_move(board,player)
        moves += 1
        print_board(board)
        winner = find_winner(board)
        if winner != 0:
            print("the winner is player {0}".format(player_tokens[winner]))
            break
        player = next_player(player)
        if moves >= 42:
            print("TIE!")
            break
            

def tests():
    '''
    >>> tests() # doctest:+ELLIPSIS
    PASS...
    True
    '''
    passed = True
    for player_a in [1,2]:
        player_b = next_player(player_a)

        # Test column win
        board = empty_board()
        make_move(board,player_a,6)
        make_move(board,player_b,5)
        make_move(board,player_a,6)
        make_move(board,player_b,4)
        make_move(board,player_a,6)
        make_move(board,player_b,3)
        make_move(board,player_a,6)
        winner = find_winner(board)
        if winner != player_a:
            print_board(board)
            print('FAIL: didn\'t detect {} won on a column'.format(player_tokens[player_a]))
            passed = False
        else:
            print('PASS: player {0} detected column'.format(player_tokens[winner]))

        # Test diag win
        board = empty_board()
        make_move(board,player_b,5)
        make_move(board,player_b,5)
        make_move(board,player_b,5)
        make_move(board,player_b,4)
        make_move(board,player_b,4)
        make_move(board,player_b,3)
        make_move(board,player_a,2)
        make_move(board,player_a,3)
        make_move(board,player_a,4)
        make_move(board,player_a,5)
        winner = find_winner(board)
        if winner != player_a:
            print_board(board)
            print("FAIL: did not detect diag winning condition")
            passed = False
        else:
            print("PASS: player {0} detected diag win".format(player_tokens[winner]))

        # Test back diag win
        board = empty_board()
        make_move(board,player_b,5)
        make_move(board,player_b,4)
        make_move(board,player_b,4)
        make_move(board,player_b,3)
        make_move(board,player_b,3)
        make_move(board,player_b,3)
        make_move(board,player_a,6)
        make_move(board,player_a,5)
        make_move(board,player_a,4)
        make_move(board,player_a,3)
        winner = find_winner(board)
        if winner != player_a:
            print_board(board)
            print("FAIL: did not back diag detect winning condition")
            passed = False
        else:
            print("PASS: player {0} detected back diag win".format(player_tokens[winner]))

    # Test if player_a will block player_B's winning move
    for player_a in [1,2]:
        player_b = next_player(player_a)
        board = empty_board()
        make_move(board,player_b,0)
        make_move(board,player_b,1)
        make_move(board,player_b,3)
        make_move(board,player_a,6)
        make_move(board,player_a,5)
        make_move(board,player_a,4)
        best_move(board,player_a)
        winner = find_winner(board)
        if board[0][2] != player_a:
            print_board(board)
            print('FAILED: player_a did not block player_b\'s winning move')
            passed = False
        else:
            print('PASS: player_a blocked player_b\'s winning move')

    # Test if player_a can find the winning move
    for player_a in [1,2]:
        player_b = next_player(player_a)
        board = empty_board()
        make_move(board,player_b,5)
        make_move(board,player_b,4)
        make_move(board,player_b,4)
        make_move(board,player_b,3)
        make_move(board,player_b,3)
        make_move(board,player_b,3)
        make_move(board,player_a,6)
        make_move(board,player_a,5)
        make_move(board,player_a,4)
        best_move(board,player_a)
        winner = find_winner(board)
        if winner != player_a:
            print_board(board)
            print('FAILED: player_a did not detect winning move')
        else:
            print("PASSED: the winner is player {0}".format(player_tokens[winner]))

    return passed

tests()
computer_vs_computer()
