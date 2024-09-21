from collections import defaultdict

def kosaraju(edges):
    graph = defaultdict(list)
    transposed = defaultdict(list)
    vertices = set()

    # Building the graph and its transpose
    for src, dest in edges:
        graph[src].append(dest)
        transposed[dest].append(src)
        vertices.add(src)
        vertices.add(dest)
    
    # First DFS to fill the stack based on finishing times
    def dfs_one(vertex, visited, stack):
        visited.add(vertex)
        for nei in graph[vertex]:
            if nei not in visited:
                dfs_one(nei, visited, stack)
        stack.append(vertex)
    
    # Stack to store the order of completion
    stack = []
    visited = set()
    for vertex in vertices:
        if vertex not in visited:
            dfs_one(vertex, visited, stack)

    # Second DFS on the transposed graph to find SCCs
    def dfs_two(vertex, visited, component):
        visited.add(vertex)
        component.append(vertex)
        for nei in transposed[vertex]:
            if nei not in visited:
                dfs_two(nei, visited, component)
    
    # Find all SCCs
    visited.clear()
    scc_list = []
    while stack:
        v = stack.pop()
        if v not in visited:
            component = []
            dfs_two(v, visited, component)
            scc_list.append(component)
    
    return scc_list