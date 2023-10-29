# AiSign = 0, userSign = 1
import copy

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
    return True if row [0] != -1 and row.count(row[0]) == 3 else False

def Winner(gameMatrix):
    rows = gameMatrix + getDiagonal(gameMatrix) + getColumns(gameMatrix)
    for row in rows:
        currentPlayer = row[0]
        if currentPlayer != -1 and checkThree(row):
            print(f"CURRENT PLAYER -> {currentPlayer}")
            return currentPlayer
    return -1

# Returns the winner if there is a winner, returns true if no one has won but all the tiles are filled, returns false if game is not over
def gameOver(gameMatrix):
    winner = Winner(gameMatrix)
    print(f"Winner -> {winner}")
    if winner != -1:
        print("GAme over returns -> ", winner)
        return winner
    if all(all(j != -1 for j in i)for i in gameMatrix):
        print("GAme over returns -> ", True)
        return True
    print("GAme over returns -> ", False)
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
    vall = 9999999
    best = -1
    print(actions(gameMatrix))
    for action in actions(gameMatrix):
        maxVal = maxValue(result(gameMatrix, action), alpha, beta)[0]
        if maxVal < vall:
            best = action
            vall = maxVal
        beta = min(beta, vall)
        if beta <= alpha:
            break
    print("In Min function : ", "vall -> ", vall, "best -> ", best)
    return vall, best

def maxValue(gameMatrix, alpha, beta):
    if gameOver(gameMatrix) == True:
        return -1, -1
    elif gameOver(gameMatrix) != False:
        return gameOver(gameMatrix), -1
    vall = -9999999
    best = -1
    print(actions(gameMatrix))
    for action in actions(gameMatrix):
        print(action)
        minVal = minValue(result(gameMatrix, action), alpha, beta)[0]
        if minVal > vall:
            best = action
            vall = minVal
        alpha = max(beta, vall)
        if beta <= alpha:
            break
    print("In Max function : ", "vall -> ", vall, "best -> ", best)
    return vall, best

# Returns optimal action
def minimax(gameMatrix):
    if gameOver(gameMatrix) == True:
        return -1
    newMatrix = copy.deepcopy(gameMatrix)
    return maxValue(newMatrix, -9999999, 9999999)[1]

def displayGame(gameMatrix):
    for row in gameMatrix:
        print(row)

gameMatrix = [[-1, -1, -1],
              [-1, -1, -1], 
              [-1, -1, -1]]

while True:
    if gameOver(gameMatrix) == True:
        break

    # Your turn
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

    # Check if the game is over after your move
    if gameOver(gameMatrix):
        break

    # AI's turn
    x = minimax(gameMatrix)
    if x == -1:
        displayGame(gameMatrix)
        break
    else:
        print("Before playMove --> ")
        displayGame(gameMatrix)
        playMove(gameMatrix, x[0], x[1], 0)
        print("After playMove --> ")
        displayGame(gameMatrix)
    displayGame(gameMatrix)
