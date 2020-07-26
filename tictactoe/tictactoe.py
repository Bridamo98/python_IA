"""
Tic Tac Toe Player
"""

import math
from copy import copy, deepcopy

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
    x_s = 0
    o_s = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == X:
                x_s = x_s + 1
            elif board[i][j] == O:
                o_s = o_s + 1
    if x_s > o_s:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result_state = deepcopy(board)
    if result_state[action[0]][action[1]] == EMPTY:
        result_state[action[0]][action[1]] = player(board)
    else:
        raise NameError('Not possible action')
    return result_state


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X) or (board[2][0] == X and board[1][1] == X and board[0][2] == X):
        return X
    if (board[0][0] == O and board[1][1] == O and board[2][2] == O) or (board[2][0] == O and board[1][1] == O and board[0][2] == O):
        return O
    for i in range(0, 3):
        if (board[i][0] == X and board[i][1] == X and board[i][2] == X) or (board[0][i] == X and board[1][i] == X and board[2][i] == X):
            return X
        if (board[i][0] == O and board[i][1] == O and board[i][2] == O) or (board[0][i] == O and board[1][i] == O and board[2][i] == O):
            return O


def board_is_full(board):
    """
    Returns True if board is full, False otherwise.
    """
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                return False
    return True


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    possible_winner = winner(board)
    if (possible_winner is not None) or (board_is_full(board)):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    _winner = winner(board)
    if _winner == X:
        return 1
    elif _winner == O:
        return -1
    else:
        return 0

def max_value_action(board):
    if terminal(board):
        return (utility(board), None, None)
    max_v = -math.inf
    best_action_i = None
    best_action_j = None
    for action in actions(board):
        opponent_v, action_i, action_j = min_value_action(result(board, action)) 
        if(max_v < opponent_v):
            max_v = opponent_v
            best_action_i = action[0]
            best_action_j = action[1]
    return (max_v, best_action_i, best_action_j)


def min_value_action(board):
    if terminal(board):
        return (utility(board), None, None)
    min_v = math.inf
    best_action_i = None
    best_action_j = None
    for action in actions(board):
        opponent_v, action_i, action_j = max_value_action(
            result(board, action))
        if(min_v > opponent_v):
            min_v = opponent_v
            best_action_i = action[0]
            best_action_j = action[1]
    return (min_v, best_action_i, best_action_j)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if not terminal(board):
        current_player = player(board)
        if current_player == X:
            v, i, j = max_value_action(board)
            return (i, j)
        else:
            v, i, j = min_value_action(board)
            return (i, j)
    else:
        return None
