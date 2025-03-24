from collections import defaultdict

def countComponents(self, n, edges):
    # this is for an undirected graph. 
    visited = set() 
    components = [] # store all connected components.

    graph = defaultdict(list)
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)

    
    # perform a classic dfs.
    def dfs(graph, node, component):
        visited.add(node)
        component.append(node)
        for nei in graph[node]:
            if nei not in visited:
                dfs(graph, nei, component)
    
    
    # for the total amount of nodes in the graph
    # this is important, because we are trying to 
    # figure out if our dfs can reach every single 
    # possible node in the graph, so we should 
    # go through all of them, since there is 
    # no guarantee that they are going to 
    # be connected.

    totalComp = 0
    for node in range(n):
        if node not in visited:
            component = []
            dfs(graph, node, component)
            components.append(component)
            totalComp += 1
    print(components)
    return totalComp