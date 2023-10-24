import math
from copy import deepcopy
import numpy as np

X = "X"
O = "O"

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

def player(board):
    #     Returns player who has the next turn on the board
    countX = 0
    countO = 0
    for i in board:
        for j in i:
            if j == "X":
                countX = countX + 1
            if j == "O":
                countO = countO + 1
    return O if countX > countO else X

def actions(board):
    #      Returns set of all possible actions (i, j) available on the board
    action = set()
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if (val == None):
                action.add((i, j))
    return action

def result(board, action):
    #      Returns the board that results from making move (i, j) on the board
    i,j = action
    if board[i][j] != None:
        return Exception("Invalid Move")
    nextMove = player(board)
    deepBoard = deepcopy(board)
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
    #       Returns 1 if X has won, -1 if O has won, 0 otherwise
    xx = winner(board)
    if xx == X:
        return 1
    elif xx == O:
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
    if player(board) == X:
        return maxAlphaBetaPruning(board, float("-inf"), float("inf"))[1]
    elif player(board) == O:
        return maxAlphaBetaPruning(board, float("-inf"), float("inf"))[1]
    else:
        raise Exception("Error in calculating optimal move")

import pygame
import sys
import time

pygame.init()
size = width, height = 600, 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("Font.ttf", 28)
largeFont = pygame.font.Font("Font.ttf", 40)
moveFont = pygame.font.Font("Font.ttf", 60)

user = None
board = initialState()
ai_turn = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    # Let user choose a player.
    if user is None:

        # Draw title
        title = largeFont.render("Play Tic-Tac-Toe", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Draw buttons
        playXButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)
        playX = mediumFont.render("Play as X", True, black)
        playXRect = playX.get_rect()
        playXRect.center = playXButton.center
        pygame.draw.rect(screen, white, playXButton)
        screen.blit(playX, playXRect)

        playOButton = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)
        playO = mediumFont.render("Play as O", True, black)
        playORect = playO.get_rect()
        playORect.center = playOButton.center
        pygame.draw.rect(screen, white, playOButton)
        screen.blit(playO, playORect)

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                time.sleep(0.2)
                user = X
            elif playOButton.collidepoint(mouse):
                time.sleep(0.2)
                user = O

    else:

        # Draw game board
        tile_size = 80
        tile_origin = (width / 2 - (1.5 * tile_size),
                       height / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 3)

                if board[i][j] != None:
                    move = moveFont.render(board[i][j], True, white)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)

        game_over = terminal(board)
        current_player = player(board)

        # Show title
        if game_over:
            winner = winner(board)
            if winner is None:
                title = f"Game Over: Tie."
            else:
                title = f"Game Over: {winner} wins."
        elif user == player:
            title = f"Play as {user}"
        else:
            title = f"Computer thinking..."
        title = largeFont.render(title, True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

        # Check for AI move
        if user != player and not game_over:
            if ai_turn:
                time.sleep(0.5)
                move = minimax(board)
                board = result(board, move)
                ai_turn = False
            else:
                ai_turn = True

        # Check for a user move
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and user == player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if (board[i][j] == None and tiles[i][j].collidepoint(mouse)):
                        board = result(board, (i, j))

        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            again = mediumFont.render("Play Again", True, black)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, white, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    user = None
                    board = initialState()
                    ai_turn = False

    pygame.display.flip()