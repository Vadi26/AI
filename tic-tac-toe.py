# AiSign = 0, userSign = 1

minMaxBit = True

def getColumns(gameMatrix):
    columns = []
    for i in range(3):
        columns.append([row[i] for row in gameMatrix])
    return columns

def getDiagonal(gameMatrix):
    return [[gameMatrix[0][0], gameMatrix[1][1], gameMatrix[2][2]], 
            [gameMatrix[0][2], gameMatrix[1][1], gameMatrix[2][0]]]

def checkThree(row):
    return True if row.count(row[0]) == 3 else False

def Winner(gameMatrix):
    rows = gameMatrix + getDiagonal(gameMatrix) + getColumns(gameMatrix)
    for row in rows:
        currentPlayer = row[0]
        if currentPlayer != -1 and checkThree(row):
            return currentPlayer
    return -1

# Returns the winner if there is a winner, returns true if no one has won but all the tiles are filled, returns false if game is not over
def gameOver(gameMatrix):
    winner = Winner(gameMatrix)
    if winner != -1:
        return winner
    if all(all(j != -1 for j in i)for i in gameMatrix):
        return True
    return False

# Returns set of all possible actions (i, j) available on the board
def actions(gameMatrix):
    action = set()
    for i, row in enumerate(gameMatrix):
        for j, val in enumerate(row):
            if (val == -1):
                action.add((i, j))
    return action

def result(gameMatrix, action):
    #      Returns the board that results from making move (i, j) on the board
    i,j = action
    if gameMatrix[i][j] != -1:
        return Exception("Invalid Move")
    gameMatrix[i][j] = 0
    return gameMatrix

def playMove(gameMatrix, i, j, player):
    i = int(i)
    j = int(j)
    if gameMatrix[i][j] != -1:
        print("Invalid Move !")
        return False, 
    gameMatrix[i][j] = player
    return True, gameMatrix

def minValue(gameMatrix, alpha, beta):
    if gameOver(gameMatrix) == True:
        return -1, -1
    elif gameOver(gameMatrix) != False:
        return gameOver(gameMatrix), -1
    vall = float("inf")
    best = -1
    for action in actions(gameMatrix):
        maxVal = maxValue(result(gameMatrix, action), alpha, beta)[0]
        if maxVal < vall:
            best = action
            vall = maxVal
        beta = min(beta, vall)
        if beta <= alpha:
            break
    return vall, best

def maxValue(gameMatrix, alpha, beta):
    if gameOver(gameMatrix) == True:
        return -1, -1
    elif gameOver(gameMatrix) != False:
        return gameOver(gameMatrix), -1
    vall = float("-inf")
    best = -1
    for action in actions(gameMatrix):
        minVal = minValue(result(gameMatrix, action), alpha, beta)[0]
        if minVal > vall:
            best = action
            vall = minVal
        alpha = max(beta, vall)
        if beta <= alpha:
            break
    return vall, best

# Returns optimal action
def minimax(gameMatrix):
    if gameOver(gameMatrix):
        return -1
    return maxValue(gameMatrix, float("-inf"), float("inf"))[1]

def displayGame(gameMatrix):
    for row in gameMatrix:
        print(row)

gameMatrix = [[-1, -1, -1],
              [-1, -1, -1], 
              [-1, -1, -1]]

while True:
    if gameOver(gameMatrix) == True:
        break
    coords = input("Enter the coordinates of the tile you want to place X : ")
    i = coords[0]
    j = coords[3]
    temp, new = playMove(gameMatrix, i, j, 1)
    while temp == False:
        coords = input("Enter the coordinates of the tile you want to place X : ")
        i = int(coords[0])
        j = int(coords[3])
        temp, new = playMove(gameMatrix, i, j, 1)
    gameMatrix = new
    displayGame(gameMatrix)
    x = minimax(gameMatrix)
    if x == -1:
        break
    else:
        playMove(gameMatrix, x[0], x[1], 0)
    displayGame(gameMatrix)