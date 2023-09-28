from tabulate import tabulate

def sortNodes(nodeList):
    nodeList.sort(key=lambda x: x[1])
    return nodeList

def isInList(N, List):
    for i in List:
        temp, _ = i
        if N == temp:
            return True
    return False

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
            print("Cost to reach the destination : ", cost)
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
                        path[child] = N
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

start = 'S'
goal = 'G'

# searchSpace = {
#     'a': [('b',1)],
#     'b': [('e',2),('c',1)],
#     'c': [('b',1),('d',6)],
#     'd': [('c',6),('f',1)],
#     'e': [('g',1),('f',2), ('b',2)],
#     'f': [('e',2),('h',1),('d',1)],
#     'g': [('h',1),('e',1)],
#     'h': [('g',1),('f',1)]
# }

searchSpace = {'A':[],
               'B':[('A',2)],
               'C':[('A',1)],
               'D':[('C',8),('E',2),('B',1)],
               'E':[('R',2),('H',8)],
               'F':[('G',2),('C',3)],
               'G':[],
               'H':[('Q',5),('P',7)],
               'P':[('Q',15)],
               'Q':[],
               'R':[('F',1)],
               'S':[('D',3),('E',9),('P',1)]
}

# searchSpace = {
#     'a': [('b',3),('c',5),('d',1)],
#     'b': [('i',9),('c',3),('a',3)],
#     'c': [('b',3),('i',4),('h',5),('g',8),('f',10),('e',5),('d',4),('a',5)],
#     'd': [('a',1),('c',4),('e',2)],
#     'e': [('d',2),('c',5),('f',2)],
#     'f': [('g',1),('e',2),('c',10)],
#     'g': [('h',5),('f',1),('c',8)],
#     'h': [('i',11),('g',5),('c',5)],
#     'i': [('h',11),('c',4),('b',9)]
# }

UCS(start, goal, searchSpace)

