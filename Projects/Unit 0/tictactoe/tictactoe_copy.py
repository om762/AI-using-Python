"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count = x_count + 1
            elif board[i][j] == O:
                o_count = o_count + 1
    
    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    
    return moves


def valid(action, board) -> bool:
    if len(action) != 2:
        return False
    
    r, c = action
    if (r in list(range(3))) and (c in list(range(3))) and board[r][c] == EMPTY:
        return True
    else:
        return False


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not valid(action, board):
        raise Exception("Invalid Action")
    
    val = player(board)
    i, j = action
    newBoard = copy.deepcopy(board)
    newBoard[i][j] = val
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    d1 = []
    d2 = []
    the_winner = None
    for i in range(3):
        # Any row
        if board[i] == [X]*3:
            the_winner = X
            break
        
        elif board[i] == [O]*3:
            the_winner = O
            break
        
        elif [board[i][0], board[i][1], board[i][2]] == [X]*3:
            the_winner = X
            break
            
        elif [board[i][0], board[i][1], board[i][2]] == [O]*3:
            the_winner = O
            break
        
        else:
            pass
        
        d1.append(board[i][i])
        d2.append(board[i][2-i])
    
    if d1 == [X]*3 or d2 == [X]*3:
        the_winner = X
    elif d1 == [O]*3 or d2 == [O]*3:
        the_winner = O
    
    return  the_winner




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    else:
        for row in board:
            if EMPTY in row:
                return False
        return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if not terminal(board):
        raise Exception("The game is still in progress")
    
    if winner(board) == X:
        return 1
    
    elif winner(board) == O:
        return - 1
    
    elif winner(board) is None:
        return 0
    
    else:
        raise Exception("Ye toh kabhi hoga hi nhi. Ho gya toh ?")


def min_value(board):
    v = -3
    
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def max_value(board):
    v = 3
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) is True:
        return None
    
    if player(board) == X:
        high_val = - 3
        best_action = list(actions(board))[0]
        for action in actions(board):
            newValue = min_value(result(board, action))
            if newValue > high_val:
                high_val = newValue
                best_action = action
    
        return best_action
    
    elif player(board) == O:
        low_val = 3
        best_action = list(actions(board))[0]
        for action in actions(board):
            newValue = max_value(result(board, action))
            if newValue < low_val:
                low_val = newValue
                best_action = action
        return best_action
    
    else:
        raise Exception("Pta nhi bhai ye hona toh nhi chahiye tha")

