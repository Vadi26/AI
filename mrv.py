import copy
import pandas as pd

def is_valid(V, visited, node, color):
    for neighbor in V[node]:
        if neighbor in visited and visited[neighbor] == color:
            return False
    return True

def mrv_ordering(V, visited, domain):
    min_remaining_values = float('inf')
    selected_node = None

    for node, colors in domain.items():
        if visited[node] is None and len(colors) < min_remaining_values:
            selected_node = node
            min_remaining_values = len(colors)

    return selected_node

def update_domain(V, visited, node, color, domain):
    for neighbor in V[node]:
        if visited[neighbor] is None and color in domain[neighbor]:
            domain[neighbor].remove(color)

def csp_filter_mrv(V, D, visited, ans, domain):
    iteration = 1
    table = pd.DataFrame(columns=visited.keys())

    def print_table():
        nonlocal table
        print(f"Iteration {iteration}:")
        print(table)
        print("\n")

    def update_table(node, color):
        nonlocal table, iteration
        table.at[iteration, node] = color

    if all(visited[node] is not None for node in visited):
        ans.append(dict(visited))
    else:
        node = mrv_ordering(V, visited, domain)
        if node is not None:
            for color in domain[node]:
                if is_valid(V, visited, node, color):
                    visited[node] = color
                    updated_domain = copy.deepcopy(domain)
                    update_domain(V, visited, node, color, updated_domain)
                    update_table(node, color)
                    print_table()
                    iteration += 1
                    csp_filter_mrv(V, D, visited, ans, updated_domain)
                    visited[node] = None

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

# Initialize domain with all colors for each node
domain = {node: list(D) for node in V.keys()}

answer = []

csp_filter_mrv(V, D, visited, answer, domain)

for solution in answer:
    print("Final Solution:")
    print(pd.DataFrame([solution]))
    print("\n")
