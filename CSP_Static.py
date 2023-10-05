import copy

def isValid(V, visited, node, color):
    for neighbor in V[node]:
        if neighbor in visited and visited[neighbor] == color:
            return False
    return True

def CSP(V, D, visited, ans, index):
    if len(V) == index:
        ans.append(dict(visited))
    else:
        nodes = list(V.keys())
        for i in range(len(D)):
            curr = nodes[index]
            node = visited[curr]
            color = D[i]
            if node is None:
                if isValid(V, visited, curr, color):
                    visited[curr] = color
                    CSP(V, D, visited, ans, index + 1)
                    visited[curr] = None

V = {
    'a': ['b', 'c'],
    'b': ['e', 'c', 'a'],
    'c': ['a', 'b', 'e', 'd'],
    'd': ['c', 'e', 'g', 'f'],
    'e': ['b', 'g', 'd', 'c'],
    'f': ['d', 'g'],
    'g': ['e', 'f', 'd']
}

visited = {
    'a': None,
    'b': None,
    'c': None,
    'd': None,
    'e': None,
    'f': None,
    'g': None
}

D = ['R', 'G', 'B']

answer = []

CSP(V, D, visited, answer, 0)

for solution in answer:
    print(solution)