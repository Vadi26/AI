from tabulate import tabulate

def givePosition(openList, cost):
    for i in range(len(openList)):
        if openList[i][1] < cost:
            continue
        elif openList[i][1] > cost:
            return i
        else:
            while i < len(openList) and openList[i][1] == cost:
                i = i + 1
            return i
    return len(openList)

def sortNodes(nodeList):
    nodeList.sort(key=lambda x: x[1])
    return nodeList

def isInClosedList(N, closedList):
    for i in closedList:
        if i == N:
            return True
    return False

def isInList(N, List):
    for i in List:
        temp, _ = i
        if N == temp:
            return True
    return False

def shouldIInsert(openList, childTuple):
    for i in range(len(openList)):
        if childTuple[0] == openList[i][0]:
            if childTuple[1] < openList[i][1]:
                openList[i][1] = childTuple[1]
                return True, i
    return False, -1

def checkCost(N, cost, openList):
    for i in range(len(openList)):
        temp, tempCost = openList[i]
        if N == temp:
            if (tempCost > cost):
                return i
    return -1

def UCS(start, goal, searchSpace):
    openList = [[start,0]]
    closedList = []
    ans = []
    path = {}

    while len(openList):
        temp=openList[:]
        N,cost = openList.pop(0)
        if N not in closedList:
            closedList.append([N,cost])

        if (N == goal):
            ans.append([temp, N, closedList, True, ""])
            break
        
        else:
            children = [list(child) for child in searchSpace[N]]
            for i in range(len(children)):
                children[i][1] += cost
            children = sortNodes(children)
            for i in range(len(children)):
                child,price = children[i]
                if (not isInList(child, closedList) and not isInList(child, openList)):
                    openList.insert(len(openList), [child, price])
                    path[child] = N
                elif isInList(child, closedList):
                    continue
                elif isInList(child,openList):
                    if (checkCost(child, price, openList) != -1):
                        openList.pop(checkCost(child, price, openList))
                        openList.insert(len(openList), [child, price])
            openList = sortNodes(openList)
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
goal = 'g'

searchSpace = {
    'a': [('b',3),('c',5),('d',1)],
    'b': [('i',9),('c',3),('a',3)],
    'c': [('b',3),('i',4),('h',5),('g',8),('f',10),('e',5),('d',4),('a',5)],
    'd': [('a',1),('c',4),('e',2)],
    'e': [('d',2),('c',5),('f',2)],
    'f': [('g',1),('e',2),('c',10)],
    'g': [('h',5),('f',1),('c',8)],
    'h': [('i',11),('g',5),('c',5)],
    'i': [('h',11),('c',4),('b',9)]
}

UCS(start, goal, searchSpace)

