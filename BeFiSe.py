import numpy as np
import math

# my logic is to create a matrix. Now an element of the matrix will be a list of two numbers. First digit will be the state of the node and the second number will be th cost or the heuristic of that node
def BeFiSe(maze, rows, cols):
    for i in range(rows):
        for j in range(cols):
            if (((i == 1) and (j == 1)) or ((i == 2) and (j == 1)) or ((i == 2) and (j == 2)) or ((i == 3) and (j == 2)) or ((i == 3) and (j == 3)) or ((i == 3) and (j == 4)) or ((i == 3) and (j == 5)) or ((i == 3) and (j == 6)) or ((i == 3) and (j == 7)) or ((i == 3) and (j == 8)) or ((i == 3) and (j == 9)) or ((i == 2) and (j == 9)) or ((i == 1) and (j == 9)) or ((i == 1) and (j == 8)) or ((i == 1) and (j == 7)) or ((i == 1) and (j == 6)) or ((i == 1) and (j == 5))):
                maze[i][j] = [-1, 0]
            
            elif (i == 2) and (j == 6):
                maze[i][j] = [2,0]
            elif (i == 3) and (j == 0):
                maze[i][j] = [1, 0]
    for i in range(rows):
        for j in range(cols):
            print(maze[i][j])

def calculateManhattan(maze, goal):
    m, n = maze.shape
    for x in range(m):
        for y in range(n):
            if (maze[x][y] != -1):
                maze[x][y] = abs(x - goal[0]) + abs(y - goal[1])
    return maze


maze = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, -1, 0, 0, 0, -1, -1, -1, -1, -1, 0],
          [0, -1, -1, 0, 0, 0, 0, 0, 0, -1, 0],
          [0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

start = [3, 0]
goal = [2, 6]

maze = calculateManhattan(maze, goal)

# So we can create a 3-tuple as follows -> [x-coord, y-coord, cost] for each node