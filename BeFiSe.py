import numpy as np
import math
import copy
import time
import tkinter as tk
from tabulate import tabulate
# # Here N is the coordinate of the block and not the actual block value

def giveNeighbors(maze, N):
    ans = []
    m, n = maze.shape
    x = N[0]
    y = N[1]
    if x > 0:
        if maze[x-1][y] != -1:
            ans.append([x - 1, y])
    if x < m - 1:
        if maze[x+1][y] != -1:
            ans.append([x + 1, y])
    if y > 0:
        if maze[x][y-1] != -1:
            ans.append([x, y - 1])
    if y < n - 1:
        if maze[x][y+1] != -1:
            ans.append([x, y + 1])
    return ans

def manhattanDistance(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def myHeuristic(node, goal):
    return max(abs(node[0] - goal[0]), abs(node[1] - goal[1])) + (math.sqrt(2) - 1) * min(abs(node[1] - goal[1]), abs(node[0] - goal[0]))

def sortNodes(openList, goal):
    opcopy = copy.copy(openList)
    for i in opcopy:
        i.append(manhattanDistance(i, goal))
    opcopy.sort(key=lambda x: x[2])
    for i in opcopy:
        i.pop(2)
    return opcopy

def BestFS(maze, start, goal):
    openList = [start]
    closedList = []
    ans = []
    path = {}
    while len(openList):
        temp = openList[:]
        N = openList.pop(0)

        if N not in closedList and N not in openList:
            closedList.append(N)

        if N == goal:
            ans.append([temp, N, closedList, True, ""])
            break
            # return
        
        else:
            children = giveNeighbors(maze, N)
            for node in children:
                if node not in closedList and node not in openList:
                    openList.append(node)
                    path[tuple(node)] = N
            openList = sortNodes(openList, goal)
            ans.append([list(temp), N, list(closedList), False, list(children)])
    print(tabulate(ans, headers=["OL", "N", "CL", "GT(N)", "Successor(N)"], tablefmt="fancy_grid"))
    finalPath = []
    curr = tuple(goal)
    while tuple(curr) != tuple(start):
        finalPath.append(tuple(curr))
        curr = path[tuple(curr)]
    finalPath.append(tuple(start))
    finalPath.reverse()
    print("Path followed is : ", finalPath)
    return finalPath, closedList

def calculateManhattan(maze, goal):
    m, n = maze.shape
    for x in range(m):
        for y in range(n):
            if (maze[x][y] != -1):
                maze[x][y] = abs(x - goal[0]) + abs(y - goal[1])
    return maze

maze = np.array([
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
    [-1, 0, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, 0, 0, -1],
    [-1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1],
    [-1, -1, -1, -1, 0, -1, -1, -1, 0, -1, -1, -1, 0, -1, -1],
    [-1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, -1, -1],
    [-1, 0, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, 0, 0, -1],
    [-1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, -1],
    [-1, 0, -1, 0, -1, -1, -1, 0, -1, -1, 0, -1, 0, 0, -1],
    [-1, 0, -1, 0, 0, 0, -1, 0, 0, -1, 0, -1, -1, -1, -1],
    [-1, 0, -1, -1, -1, 0, -1, -1, -1, -1, 0, 0, 0, 0, -1],
    [-1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, -1, 0, -1],
    [-1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, -1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
])

# maze = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#           [0, -1, 0, 0, 0, -1, -1, -1, -1, -1, 0],
#           [0, -1, -1, 0, 0, 0, 0, 0, 0, -1, 0],
#           [0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

start = [1, 1]
goal = [12, 13]

maze = calculateManhattan(maze, goal)
print(maze)

path, visited = BestFS(maze, start, goal)

def giveWalls(maze):
    m, n = maze.shape
    ans = []
    for x in range(m):
        for y in range(n):
            if (maze[x][y] == -1):
                ans.append((x,y))
    return ans

# walls = [(1,1), (2,1), (2,2), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7), (3,8), (3,9), (2,9), (1,9), (1,8), (1,7), (1,6), (1,5)]
walls = giveWalls(maze)
def createMaze(canvas, rows, cols, square_size):
    st = tuple(start)
    go = tuple(goal)
    for i in range(rows):
        for j in range(cols):
            x1 = j * square_size
            y1 = i * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size
            canvas.create_rectangle(x1, y1, x2, y2, fill='white')
    for i in range(rows):
        for j in range(cols):
            x1 = j * square_size
            y1 = i * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size
            if (i,j) in walls:
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
            elif (i,j) == st:
                canvas.create_rectangle(x1, y1, x2, y2, fill='red')
            elif (i,j) == go:
                canvas.create_rectangle(x1, y1, x2, y2, fill='green')

def Animate(canvas, visited, delay=500, index=1):
    if index == len(visited) - 1:
        return
    if index < len(visited):
        i, j = visited[index]
        x1 = j * square_size
        y1 = i * square_size
        x2 = x1 + square_size
        y2 = y1 + square_size
        canvas.create_rectangle(x1, y1, x2, y2, fill='blue')
        canvas.after(delay, lambda: Animate(canvas, visited, delay, index + 1))

root = tk.Tk()
root.title("Robot navigation using Greedy Best First Search")

canvas = tk.Canvas(root, width=500, height=500)  
canvas.pack()
rows = 15
cols = 15
square_size = min(500 // cols, 500 // rows)
createMaze(canvas, rows, cols, square_size)
Animate(canvas, visited)
root.mainloop()