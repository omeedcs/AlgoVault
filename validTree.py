from collections import deque

# this is a bfs solution. 
# its trivial, if we visited all the nodes (N), that means all the 
# nodes are connected.
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        # Build the graph
        graph = {i: [] for i in range(n)}
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)  # Add this line for undirected graph
        
        visited = set()
        queue = deque()
        queue.append(0)
        
        while queue:
            node = queue.popleft()
            if node in visited:
                return False  # Cycle detected
            visited.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    queue.append(nei)
        
        return len(visited) == n  # Check if all nodes are connected