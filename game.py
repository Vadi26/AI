import numpy as np
import copy

USER = 1
AI = 0

def initialState():
    return [[None, None, None],
            [None, None, None],
            [None, None, None]]

def getDiagonal(board):
    return [[board[0][0], board[1][1], board[2][2]], 
            [board[0][2], board[1][1], board[2][0]]]

def getColumns(board):
    columns = []
    for i in range(3):
        columns.append([row[i] for row in board])
    return columns

def threeInARow(row):
    return True if row.count(row[0]) == 3 else False

def actions(board):
    #      Returns set of all possible actions (i, j) available on the board
    action = set()
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if (val == None):
                action.add((i, j))
    return action

def player(board):
    #     Returns player who has the next turn on the board
    countX = 0
    countO = 0
    for i in board:
        for j in i:
            if j == 1:
                countX = countX + 1
            if j == 0:
                countO = countO + 1
    return AI if countX > countO else USER

def result(board, action):
    #      Returns the board that results from making move (i, j) on the board
    i,j = action
    if board[i][j] != None:
        return Exception("Invalid Move")
    nextMove = player(board)
    deepBoard = copy.deepcopy(board)
    deepBoard[i][j] = nextMove
    return deepBoard

def winner(board):
    rows = board + getDiagonal(board) + getColumns(board)
    for row in rows:
        currentPlayer = row[0]
        if currentPlayer is not None and threeInARow(row):
            return currentPlayer
    return None

def terminal(board):
    #        Returns true if game is over, false otherwise
    xx = winner(board)
    if xx is not None:
        return True
    if all(all(j != None for j in i)for i in board):
        return True
    return False

def utility(board):
    #       Returns 1 if USER has won, -1 if AI has won, 0 otherwise
    xx = winner(board)
    if xx == USER:
        return 1
    elif xx == AI:
        return -1
    else:
        return 0

def maxAlphaBetaPruning(board, alpha, beta):
    if terminal(board) == True:
        return utility(board), None
    vall = float("-inf")
    best = None
    for action in actions(board):
        minValue = minAlphaBetaPruning(result(board, action), alpha, beta)[0]
        if minValue > vall:
            best = action
            vall = minValue
        alpha = max(beta, vall)
        if beta <= alpha:
            break
    return vall, best

def minAlphaBetaPruning(board, alpha, beta):
    if terminal(board) == True:
        return utility(board), None
    vall = float("inf")
    best = None
    for action in actions(board):
        maxValue = maxAlphaBetaPruning(result(board, action), alpha, beta)[0]
        if maxValue < vall:
            best = action
            vall = maxValue
        beta = min(beta, vall)
        if beta <= alpha:
            break
    return vall, best

def minimax(board):
    #       Returns optimal action for the current player on the board
    if terminal(board):
        return None
    if player(board) == USER:
        return maxAlphaBetaPruning(board, float("-inf"), float("inf"))[1]
    elif player(board) == AI:
        return maxAlphaBetaPruning(board, float("-inf"), float("inf"))[1]
    else:
        raise Exception("Error in calculating optimal move")

def playMove(gameMatrix, i, j, player):
    i = int(i)
    j = int(j)
    if gameMatrix[i][j] is not None:
        print("Invalid Move !")
        return False, None
    gameMatrix[i][j] = player
    return True, gameMatrix

def displayGame(gameMatrix):
    for row in gameMatrix:
        print(row)

gameMatrix = [[None, None, None],
            [None, None, None],
            [None, None, None]]

user = None

while True:
    gameOver = terminal(gameMatrix)
    currentPlayer = player(gameMatrix)

    if gameOver:
        winner = winner(gameMatrix)
        if winner is None:
            print("Game over : TIE")
        else:
            print(f"Game over : {winner} wins")
    
    coords = input("Enter the coordinates of the tile you want to place X : ")
    i = int(coords[0])
    j = int(coords[3])
    temp, new = playMove(gameMatrix, i, j, 1)
    while temp == False:
        coords = input("Enter the coordinates of the tile you want to place X : ")
        i = int(coords[0])
        j = int(coords[3])
        temp, new = playMove(gameMatrix, i, j, 1)
    gameMatrix = new
    displayGame(gameMatrix)

    move = minimax(gameMatrix)
    if move is not None:
        gameMatrix = result(gameMatrix, move)
        displayGame(gameMatrix)
    else:
        winner = winner(gameMatrix)
        if winner is None:
            print("Game over : TIE")
        else:
            print(f"Game over : {winner} wins")
        break