"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None
set_minus = {(0,0),(0,1),(0,2),(1,0),(2,0),(1,2),(2,1),(1,1),(2,2)}

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
    count_o = 0
    for row in board:
        count_x += row.count('X')
        count_o += row.count('O')
    if count_x <= count_o:
        return 'X'
    else:
        return 'O'

def actions(board) -> set:
    able = set()
    for i, row in enumerate(board):  # for문과 동일
        for j, col in enumerate(row):
            if board[i][j] is None:
                able.add((i,j))
    return able

def result(board, action):
    #action 튜플
    """
    Returns the board that results from making move (i, j) on the board.
    """
    cp_board = copy.deepcopy(board)
    if action in actions(cp_board):
        row, col = action
        cp_board[row][col] = player(cp_board)
    else:
        raise Exception('Wrong Move')
    return cp_board


def winner(board):
    """
    Returns the winner of the game, if there is one.

    print(set_minus - actions(board))
    try:
        for tuple in (set_minus - actions(board)):
            x1, y1 = tuple
            list_dx = [-1, 1, -1, 1, 0, 0, 1, -1]
            list_dy = [0, 0, -1, 1, -1, 1, -1, 1]
            for i in range(0, len(list_dx), 2):
                cnt = 1
                for j in range(i, i + 2):
                    dx, dy = list_dx[j], list_dy[j]
                    x, y = x1, y1
                    while True:
                        x, y = x + dx, y + dy
                        print(x,y)
                        if (x < 0 or x >= 3 or y < 0 or y >= 3) or (board[x][y] != board[x1][y1]):
                            break;
                        else:
                            cnt += 1
                print(cnt)
                if cnt >= 3:
                    return board[x1][y1]
            return None
    except:
        return None
    """


    if (board[0] == player(board) and board[1] == player(board) and board[2] == player(board)) or \
        (board[3] == player(board) and board[4] == player(board) and board[5] == player(board)) or \
        (board[6] == player(board) and board[7] == player(board) and board[8] == player(board)) or \
        (board[0] == player(board) and board[3] == player(board) and board[6] == player(board)) or \
        (board[1] == player(board) and board[4] == player(board) and board[7] == player(board)) or \
        (board[2] == player(board) and board[5] == player(board) and board[8] == player(board)) or \
        (board[0] == player(board) and board[4] == player(board) and board[8] == player(board)) or \
        (board[2] == player(board) and board[4] == player(board) and board[6] == player(board)):
        return True
    else:
        return False



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #winner 사용
    if len(actions(board))==0 or winner(board) is not None:
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


#https://gist.github.com/yigitpirildak/0b9b1a0447ab87c749ea4c8f8948c4c2 참조

def minimax(board):
    #action 튜플 반환
    """
    Returns the optimal action for the current player on the board.
    """
    if not terminal(board):
        bestscore = -math.inf
        bestmove = None
        for move in actions(board):
            board = result(board, move)
            curr_score = helper(False, board)
            print(curr_score)
            if (curr_score > bestscore):
                bestscore = curr_score
                bestmove = move
        return bestmove

def helper(maxturn, board):
    if terminal(board):
        state = utility(board)
        return state

    score= []
    for move in actions(board):
        board = result(board, move)
        score.append(helper(not maxturn, board))

    return max(score) if maxturn else min(score)
