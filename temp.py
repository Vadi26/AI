# def is_valid(node, color, V, assignment):
#     for neighbor in V[node]:
#         if neighbor in assignment and assignment[neighbor] == color:
#             return False
#     return True

# def CSP(V, D, assignment):
#     if len(assignment) == len(V):
#         print("Solution found:")
#         for node, color in assignment.items():
#             print(f"{node}: {color}")
#         print()
#         return

#     node = list(V.keys())[len(assignment)]
#     # node = list(V.keys())
#     print("Node is this --> ", node)
#     for color in D:
#         if is_valid(node, color, V, assignment):
#             assignment[node] = color
#             CSP(V, D, assignment)
#             assignment.pop(node)

# V = {
#     'a': ['b', 'c'],
#     'b': ['a', 'c', 'd', 'e'],
#     'c': ['a', 'b', 'd', 'f'],
#     'd': ['b', 'c', 'e', 'f'],
#     'e': ['b', 'd'],
#     'f': ['c', 'd']
# }

# D = ['R', 'G', 'B']

# CSP(V, D, {})

def isValid(V, visited, node, color):
    for neighbor in V[node]:
        if neighbor in visited and visited[neighbor] == color:
            return False
    return True

def CSP(V, D, visited, ans, index):
    if len(V) == index:
        print(visited)
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
                    visited[curr] = None  # Reset visited[curr] after recursion

V = {'a': ['b', 'c'],
     'b': ['a', 'c', 'd', 'e'],
     'c': ['a', 'b', 'd', 'f'],
     'd': ['b', 'c', 'e', 'f'],
     'e': ['b', 'd'],
     'f': ['c', 'd']}

visited = {'a': None,
           'b': None,
           'c': None,
           'd': None,
           'e': None,
           'f': None}

D = ['R', 'G', 'B']

answer = []
CSP(V, D, visited, answer, 0)

# Print all solutions
for solution in answer:
    print(solution)
