def is_valid(node, color, graph, coloring):
    for neighbor in graph[node]:
        if coloring[neighbor] == color:
            return False
    return True

def ac3(graph, colors, coloring):
    queue = [(node, color) for node in graph for color in colors]

    while queue:
        node, color = queue.pop(0)
        if is_valid(node, color, graph, coloring) and coloring[node] != color:
            coloring[node] = color
            queue.extend([(n, c) for n in graph for c in colors if n != node])
    return coloring  # Return the final coloring

def backtrack_coloring(graph, colors, coloring, node_order):
    if None not in coloring.values():
        yield dict(coloring)
    else:
        node = next(node for node, color in coloring.items() if color is None)
        for color in colors:
            if is_valid(node, color, graph, coloring):
                coloring[node] = color
                yield from backtrack_coloring(graph, colors, coloring, node_order)
                coloring[node] = None
        node_order.insert(0, node)

def graph_coloring(graph, colors):
    node_order = list(graph.keys())
    solutions = list(backtrack_coloring(graph, colors, {node: None for node in graph}, node_order))
    
    if solutions:
        for solution in solutions:
            for node, color in solution.items():
                print(f"{node}: {color}  ", end="")
            print()
        print("Graph Coloring Completed Successfully.")
    else:
        print("No solution found.")

custom_graph = {
    "Node1": ["Node2", "Node3"],
    "Node2": ["Node1", "Node3", "Node4"],
    "Node3": ["Node1", "Node2", "Node4", "Node5"],
    "Node4": ["Node2", "Node3", "Node5", "Node6"],
    "Node5": ["Node3", "Node4"],
    "Node6": ["Node4"]
}
custom_colors = ['R', 'G', 'B'] 
graph_coloring(custom_graph, custom_colors)
