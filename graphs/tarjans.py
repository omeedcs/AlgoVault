def tarjans_algorithm(graph):
    index = 0  # Used to assign unique indices to each node
    index_map = {}  # Maps nodes to their index
    lowlink_map = {}  # Maps nodes to their lowlink value
    stack = []  # Stack to keep track of the current SCC
    on_stack = set()  # Set to keep track of nodes currently on the stack
    sccs = []  # List to store all the SCCs found

    def dfs(node):
        nonlocal index
        index_map[node] = index
        lowlink_map[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)

        # Consider successors of the current node
        for neighbor in graph[node]:
            if neighbor not in index_map:
                # Successor has not yet been visited; recurse on it
                dfs(neighbor)
                lowlink_map[node] = min(lowlink_map[node], lowlink_map[neighbor])
            elif neighbor in on_stack:
                # Successor is in the current SCC
                lowlink_map[node] = min(lowlink_map[node], index_map[neighbor])

        # If node is a root node, pop the stack and generate an SCC
        if lowlink_map[node] == index_map[node]:
            scc = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                scc.append(w)
                if w == node:
                    break
            sccs.append(scc)

    # Call DFS for each node that has not been visited yet
    for node in graph:
        if node not in index_map:
            dfs(node)

    return sccs

# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': ['B'],
        'B': ['C', 'E', 'F'],
        'C': ['D', 'G'],
        'D': ['C', 'H'],
        'E': ['A', 'F'],
        'F': ['G'],
        'G': ['F'],
        'H': ['D', 'G']
    }

    sccs = tarjans_algorithm(graph)
    print("Strongly connected components:", sccs)
