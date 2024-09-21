# basic graph practice.

# NOTE: potentially practice using node class, these 
# implementations are entirely list based, and assume that 
# each index inside of the list that is passed in is a node
# in and of itself. Remember,
# GRAPH is: {key, value}, key: node, value is the adjacency list.

from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self):
        # consturctor
        self.graph = defaultdict(list)
        self.vertices = set()

    def num_of_vertices(self):
        return len(self.vertices)

    def add_edge(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph[u].append(v)
    
    # DFS - no NODE CLASS
    def depth_first_search(self, v, visited):
        if visited == None:

            # we use a set to ensure that each node is 
            # only processed once.
            visited = set()

        visited.add(v)

        for node in self.graph[v]:
            visited.add(node)
            if node not in visited:
                # make the recursive call
                self.depth_first_search(node, visited)
    
    # BFS - no NODE CLASS
    def breadth_first_search(self, graph, start, visited = None):
        # add the initial node into the queue
        queue = deque()
        if visited == None:
            num_of_vertices = self.num_of_vertices()
            print("Number of vertices: ", num_of_vertices)
            visited = [False] * num_of_vertices

        # we are marking that start node.
        visited[start] = True
        queue.append(start)
        
        while queue:
            # O(1) operation because of deque
            curr_node = queue.popleft()
            print(curr_node)

            for node in self.graph[curr_node]:
                # if it is not marked
                if visited[node] == False:
                    visited[node] = True
                    queue.append(node)


graph = Graph()
graph.add_edge(0, 1)
graph.add_edge( 0, 2)
graph.add_edge( 1, 3)
graph.add_edge( 1, 4)
graph.add_edge( 2, 4)
graph.breadth_first_search(graph, 0)
