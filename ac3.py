def is_valid(node, color, V, visited):
    for neighbor in V[node]:
        if visited[neighbor] == color:
            return False
    return True

def ac3(V, D, visited):
    queue = [(node, color) for node in V for color in D]

    while queue:
        node, color = queue.pop(0)
        if is_valid(node, color, V, visited) and visited[node] != color:
            visited[node] = color
            queue.extend([(n, c) for n in V for c in D if n != node])
    return visited  # Return the final coloring

def backtrack_coloring(V, D, visited):
    if None not in visited.values():
        yield dict(visited)
    else:
        node = next(node for node, color in visited.items() if color is None)
        for color in D:
            if is_valid(node, color, V, visited):
                visited[node] = color
                yield from backtrack_coloring(V, D, visited)
                visited[node] = None

def graph_coloring(V, D):
    visited = {node: None for node in V}
    solutions = list(backtrack_coloring(V, D, visited))
    
    if solutions:
        for solution in solutions:
            for node, color in solution.items():
                print(f"{node}: {color}  ", end="")
            print()
        print("AC-3 Completed Successfully.")
    else:
        print("No solution found.")

V = {
    "Estonia": ["Russia", "Latvia"],
    "Russia": ["Estonia", "Latvia", "Belarus"],
    "Latvia": ["Estonia", "Russia", "Lithuania", "Belarus"],
    "Lithuania": ["Latvia", "Belarus", "Kaliningrad", "Poland"],
    "Belarus": ["Russia", "Latvia", "Lithuania", "Poland"],
    "Kaliningrad": ["Lithuania", "Poland"],
    "Poland": ["Lithuania", "Belarus", "Kaliningrad"]
}
D = ['R', 'G', 'B'] 
graph_coloring(V, D)