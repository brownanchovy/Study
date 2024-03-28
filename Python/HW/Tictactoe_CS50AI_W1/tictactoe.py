"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    #tictactoe 초기 상태를 리턴 2차원 배열 리스트
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_y = 0
    for row in board:
        count_x += row.count('X')
        count_y += row.count('Y')
    if count_x >= count_y:
        return 'X'
    else:
        return 'Y'


def actions(board, val):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # for문과 동일
    able = []
    for i, row in enumerate(board):  # for문과 동일
        for j, col in enumerate(row):
            if board[i][j] is val:
                able.append((i,j))
                return able
def none():
    return None
def exist():
    return not None


def result(board, action):
    #action 튜플
    """
    Returns the board that results from making move (i, j) on the board.
    """
    cp_board = copy.deepcopy(board)
    if action not in actions(cp_board, none()):
        raise Exception("That is not possible")
    else:
        row, col = action
        cp_board[row][col]=player(cp_board)
    return cp_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for tuple in actions(board, exist()):
        x, y = tuple
        x1, y1 = x, y
        list_dx = [-1, 1, -1, 1, 0, 0, 1, -1]
        list_dy = [0, 0, -1, 1, -1, 1, -1, 1]
        for i in range(0, len(list_dx), 2):
            cnt = 1
            for j in range(i, i + 2):
                dx, dy = list_dx[j], list_dy[j]
                x, y = x1, y1
                while True:
                    x, y = x + dx, y + dy
                    if board[x][y] is IndexError or board[x][y] != player(board):
                        break
                    else:
                        cnt += 1
            if cnt >= 3:
                return player(board)
        return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #winner 사용
    if actions(board,none()) == [] or winner(board) is not None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #terminal & winner 사용
    if terminal(board):
        if winner(board) == 'X': return 1
        elif winner(board) == 'O': return -1
        else: return 0


def minimax(board):
    #action 튜플 반환
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        while True:


def minium(board):
    for i in actions(board, none()):

        maxium(result(board,i))
def maxium(board):
    for i in actions(board, none()):
        minium(result(board,i))