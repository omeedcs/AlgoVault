
import collections 

def bfs(graph, start):
    queue = collections.deque()
    visited = set()
    queue.append(start)
    visited.add(start)
    bfs_order = []
    while queue:
        v = queue.popleft()
        bfs_order.append(v)
        for nei in graph[v]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)
    return bfs_order


# notes: O(V + E) time complexity. We explore all vertices
# and all edges in the graph. we say (V + E) because we look at the edges 
# that are connected to each vertex.
# This implementation assumes an adjacency list implementation.
# BFS is the baseline for Dijkstras, Kahns and Prims algo.
