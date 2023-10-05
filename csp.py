# import copy

# def check(V, vList, visited, index):
#     if index >= len(vList):
#         return True
#     else:
#         region = vList[index]
#         neighbors = V[region]
#         if neighbors is not None:
#             for neighbor in neighbors:
#                 if visited[neighbor] == visited[region]:
#                     return False
#         return True

# def CSPWithBacktracking(V, vList, D, visited, ans, index):
#     prevAns = copy.copy(ans)
#     if len(V) == index:
#         ans.append(dict(visited))
#         return
    
#     for i in range(1, D):
#         region = vList[index]
#         visited[region] = i
#         if check(V, vList, visited, index) == True:
#             CSPWithBacktracking(V, vList, D + 1, visited, ans, index + 1)
#         visited[region] = None
#     if (len(prevAns) != len(ans)):
#         CSPWithBacktracking(V, vList, D + 1, visited, ans, index + 1)
#     return

# def colorGraph(V):
#     ans = []
#     vList = list(V.keys())
#     visited = copy.copy(V)
#     for key in vList:
#         visited[key] = None
#     CSPWithBacktracking(V, vList, 2, visited, ans, 0)
#     for i in ans:
#         print(i)

# V = {'a':['b', 'c'],
#     'b':['a', 'c', 'd', 'e'],
#     'c':['a', 'b', 'd', 'f'],
#     'd':['b', 'c', 'e', 'f'],
#     'e':['b', 'd'],
#     'f':['c', 'd']}

# colorGraph(V)

import copy

def check(V, vList, visited, index):
    if index >= len(vList):
        return True
    else:
        region = vList[index]
        neighbors = V[region]
        if neighbors is not None:
            for neighbor in neighbors:
                if visited[neighbor] == visited[region]:
                    return False
        return True

def CSPWithBacktracking(V, vList, D, visited, ans, index):
    if len(vList) == index:
        ans.append(dict(visited))
        return
    
    for i in range(1, D + 1):
        region = vList[index]
        visited[region] = i
        if check(V, vList, visited, index):
            CSPWithBacktracking(V, vList, D, visited, ans, index + 1)
        visited[region] = None

def colorGraph(V):
    ans = []
    vList = list(V.keys())
    visited = {}
    for key in vList:
        visited[key] = None
    CSPWithBacktracking(V, vList, 2, visited, ans, 0)
    
    for i in ans:
        print(i)

V = {'a':['b', 'c'],
    'b':['a', 'c', 'd', 'e'],
    'c':['a', 'b', 'd', 'f'],
    'd':['b', 'c', 'e', 'f'],
    'e':['b', 'd'],
    'f':['c', 'd']}

colorGraph(V)
