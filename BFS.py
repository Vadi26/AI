from tabulate import tabulate

def BFS(start, goal, searchSpace):
    openList = [start]
    closedList = []
    ans = []
    path = {}

    while len(openList):
        temp=openList[:]
        N = openList.pop(0)
        if N not in closedList:
            closedList.append(N)

        if (N == goal):
            ans.append([temp, N, closedList, True, ""])
            break
        
        else:
            children = searchSpace[N]
            for i in range(len(children)):
                child=children[i]
                if (child not in closedList and child not in openList):
                    openList.insert(len(openList), child)
                    path[child] = N
            ans.append([temp, N, list(closedList), False, children])
    print(tabulate(ans, headers=["OL", "N", "CL", "GT(N)", "Successor(N)"], tablefmt="fancy_grid"))
    finalPath = []
    curr = goal
    while curr != start:
        finalPath.append(curr)
        curr = path[curr]
    finalPath.append(start)
    finalPath.reverse()
    print("Path followed is : ", finalPath)

start = 'a'
goal = 'h'

# searchSpace = {
#     'a': ['b'],
#     'b': ['e','c'],
#     'c': ['b','d'],
#     'd': ['c','f'],
#     'e': ['g','f','b'],
#     'f': ['e','h','d'],
#     'g': ['h','e'],
#     'h': ['g','f']
# }

searchSpace = {
    "A":["C", "B"],
    "B":["A", "D", "E"],
    "C":["A", "D"],
    "D":["B", "C", "G", "F"],
    "E":["B", "F"],
    "F":["D", "H", "E"],
    "G":["D"],
    "H":["F"],
}

BFS(start, goal, searchSpace)

