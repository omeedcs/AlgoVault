# undirected cycle detection with bfs is literally
# as simple as seeing if the visited list is the same 
# size as the number of nodes in the list. 

import collections 
def undir_cycle_detect(graph, n) -> bool:
    visited = set()
    queue = collections.deque() 
    while queue: 
        node = queue.popleft()
        if node in visited:
            return False
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                queue.append(nei)
        return len(visited) == n
    

# also fun note: number of edges in the graph is mathematically
# equivalent to the number of edges in the graph.
