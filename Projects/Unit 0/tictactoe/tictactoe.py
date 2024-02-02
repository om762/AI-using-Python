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
                x_count += 1
            elif board[i][j] == O:
                o_count += 1
            elif board[i][j] is EMPTY:
                pass
            else:
                print("There are some extra value in board")
                raise Exception("This Should happed for sure")
    if x_count <= o_count :
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
            if board[i][j] is EMPTY:
                moves.add((i, j))
            elif board[i][j] == X or board[i][j] == O:
                pass
            else:
                print("This Should happed")
                raise Exception("Extra Value")
    return moves

def valid(action, board) -> bool:
    if len(action) != 2:
        print("Invalid type of Action")
        return False
    r, c = action
    if r not in range(3) and c not in range(3):
        print("Action out of the box")
        return False
    if board[r][c] != EMPTY:
        print("Place is Already Filled")
        return False
    
    return True

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if valid(action, board):
        i, j = action
        newboard = copy.deepcopy(board)
        newboard[i][j] = player(board)
        return newboard



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if all(cell == X for cell in row):
            return X
        elif all(cell == O for cell in row):
            return O

    # Check columns
    for col in range(3):
        if all(board[row][col] == X for row in range(3)):
            return X
        elif all(board[row][col] == O for row in range(3)):
            return O

    # Check diagonals
    if all(board[i][i] == X for i in range(3)) or all(board[i][2 - i] == X for i in range(3)):
        return X
    elif all(board[i][i] == O for i in range(3)) or all(board[i][2 - i] == O for i in range(3)):
        return O

    return None  # No winner



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there is a winner
    if winner(board) is not None:
        return True

    # Check if the board is full
    if all(cell is not None for row in board for cell in row):
        return True

    return False  # Game is not over



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)

    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0  # Game is either a draw or ongoing



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None  # The game is already over

    current_player = player(board)

    if current_player == X:
        _, action = max_value(board)
        return action
    else:
        _, action = min_value(board)
        return action


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    optimal_action = None

    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > v:
            v = min_val
            optimal_action = action

    return v, optimal_action


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    optimal_action = None

    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < v:
            v = max_val
            optimal_action = action

    return v, optimal_action

