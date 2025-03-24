# in computer science, topological typically relates to 
# relationships between elements that define an order or 
# hiearchy. 
# typically, in topological sorting, we use a common
# algorithms known as kahns algorithm, which is designed
# for DIRECT, ACYCLIC GRAPHS. 

# we can topo sort in 3 different ways:
# (1): BFS O(V + E)
# (2): DFS O(V + E) 
# (3): Kahns Algorithm O(V + E)

# Toposorting can also help us with cycle detection.

# If a node has no incoming edges, it doesn't depend on any other node.
# we call those incoming edges "in-degree".
# THAT IS THE CORE IDEA OF KAHNS. 

from collections import defaultdict
from collections import deque

def kahns(self, edges, numOfNodes):
    
    graph = defaultdict(list)
    in_degrees = {}

    # NOTE: we can also do a predefined in degree array
    # for example, if we know there are 26 nodes in the 
    # graph....
    in_degrees_two = [0] * 26 # O(1) time! predefined memory.

    topologicalOrder = []

    # number of nodes in graph does not correlate to the 
    # edges list. It is typically the bounds / constraints of 
    # the actual problem space.

    for src, dest in edges:
        graph[src].append(dest)
        if dest in in_degrees:
            in_degrees[dest] += 1
        else:
            in_degrees[dest] = 0
    
    queue = deque()
    for node in in_degrees:
        if in_degrees[node] == 0:
            queue.append(node)
    
    while queue:
        node = queue.popleft()
        topologicalOrder.append(node)
        for nei in graph[node]:
            in_degrees[nei] -= 1
            if in_degrees[nei] == 0:
                queue.append(nei)
            
    if len(result) != numOfNodes:
        # we have detected a cycle
        return None 
        # or handle cycle detection based on problem space.
    else:
        return topologicalOrder # this is the topo order.
        
