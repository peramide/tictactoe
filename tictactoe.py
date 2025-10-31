"""
Tic Tac Toe Player with Minimax
"""

import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    X_Counter = sum(row.count(X) for row in board)
    O_Counter = sum(row.count(O) for row in board)
    return O if X_Counter > O_Counter else X


def actions(board):
    acts = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                acts.add((i, j))
    return acts


def result(board, action):
    if action not in actions(board):
        raise ValueError("Invalid action")
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    # Check rows
    for row in board:
        if row[0] is not None and all(cell == row[0] for cell in row):
            return row[0]

    # Check columns
    for j in range(3):
        if board[0][j] is not None and all(board[i][j] == board[0][j] for i in range(3)):
            return board[0][j]

    # Check diagonals
    if board[0][0] is not None and all(board[i][i] == board[0][0] for i in range(3)):
        return board[0][0]
    if board[0][2] is not None and all(board[i][2 - i] == board[0][2] for i in range(3)):
        return board[0][2]

    return None


def terminal(board):
    return winner(board) is not None or not any(EMPTY in row for row in board)


def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None

    if player(board) == X:
        value, move = max_value(board)
        return move
    else:
        value, move = min_value(board)
        return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        aux, _ = min_value(result(board, action))
        if aux > v:
            v, move = aux, action
            if v == 1:
                break
    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        aux, _ = max_value(result(board, action))
        if aux < v:
            v, move = aux, action
            if v == -1:
                break
    return v, move
