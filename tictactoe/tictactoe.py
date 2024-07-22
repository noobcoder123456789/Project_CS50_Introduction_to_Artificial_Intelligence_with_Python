"""
Tic Tac Toe Player
"""

import math
import copy

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
    cntX = cntY = 0
    for i in range(3):
        for j in range(3):
            cntX += board[i][j] == X
            cntY += board[i][j] == O
    
    if cntX == cntY:
        return X

    return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionSet = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actionSet.add((i, j))

    return actionSet
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0] < 0 or action[1] < 0 or action[0] > 2 or action[1] > 2:
        raise Exception    
    
    if board[action[0]][action[1]] != EMPTY:
        raise Exception

    board[action[0]][action[1]] = player(board)
    return board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    ans = utility(board)
    if ans == 1:
        return X
    elif ans == -1:
        return O
    else:
        return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if utility(board):
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == X:
            return 1
        
        if board[0][0] == O:
            return -1
        
        return 0
    
    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        if board[1][1] == X:
            return 1
        
        if board[1][1] == O:
            return -1
        
        return 0

    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        if board[0][0] == X:
            return 1
        
        if board[0][0] == O:
            return -1
        
        return 0
    
    if board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        if board[1][1] == X:
            return 1
        
        if board[1][1] == O:
            return -1
        
        return 0
    
    if board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        if board[2][2] == X:
            return 1
        
        if board[2][2] == O:
            return -1
        
        return 0
    
    if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        if board[0][0] == X:
            return 1
        
        if board[0][0] == O:
            return -1
        
        return 0
    
    if board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        if board[1][1] == X:
            return 1
        
        if board[1][1] == O:
            return -1
        
        return 0

    if board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        if board[2][2] == X:
            return 1
        
        if board[2][2] == O:
            return -1
        
        return 0

    return 0
    raise NotImplementedError

def findVal(tempBoard):
    if terminal(tempBoard):
        return utility(tempBoard)
    
    value = None
    plyer = player(tempBoard)
    if plyer == X:
        value = -1
    else:
        value = 1
    
    actionSet = actions(tempBoard)
    for action in actionSet:
        tempOfTempBoard = copy.deepcopy(tempBoard)
        tempOfTempBoard = result(tempOfTempBoard, action)
        if plyer == X:
            value = max(value, findVal(tempOfTempBoard))
        else:
            value = min(value, findVal(tempOfTempBoard))
    
    return value

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """    
    actionSet = actions(board)
    res = value = None    
    plyer = player(board)
    if plyer == X:
        value = -1
    else:
        value = 1

    for action in actionSet:
        tempBoard = copy.deepcopy(board)
        tempBoard = result(tempBoard, action)
        tempFindval = findVal(tempBoard)
        if plyer == X and tempFindval > value:
            value = tempFindval
            res = action
        elif plyer == O and tempFindval < value:
            value = tempFindval
            res = action
    
    return res
    raise NotImplementedError
