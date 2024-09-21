# this is a classic DFS in which 
# our base case is implicit. 
# implicit base case is nei not in visited. 

# at a certain point, we visit all nodes
# and then the recursion will stop executing.
# Time Complexity: O(V + E)
# Auxilary stack space is O(V), implicit during runtime.
def dfs(graph, node, visited):
    visited.add(node)
    print("Visited: ", node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(graph, nei, visited)

# Sample graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()
dfs(graph, 'A', visited) 


