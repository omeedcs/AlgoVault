from collections import defaultdict

def findRedundantConnection(edges):
    # we create a default dict to reperesent the graph.
    # we can use a set to do efficient edge checking. 
    graph = defaultdict(set)
    
    # depth first search helper.
    def dfs(src, dest, visited):
        # base case, if we reach dest we found a cycle.
        # this is cycle detection.
        if src == dest:
            return True
        
        # mark the current node as visited. 
        visited.add(src)

        # iterate over the neighbors in the graph.
        for nei in graph[src]:
            if nei not in visited:
                # if the DFS from this neighbor found 
                # the destination, we've found a cycle.
                if dfs(nei, dest, visited):
                    return True
        # if we've checked all our neighbors but we have 
        # not found a destination, then no cycle 
        # exists in the graph.
        return False
    
    # iterate through the edges. 
    for src, dest in edges:
        visited = set()
        # if both nodes are already in our graph,
        # check to see if a cycle exists with dfs.
        if src in graph and dest in graph and dfs(src, dest, visited):
            # returns the source and dest of that cycle.
            return [src, dest]
        
        # no cycle exists? its fine, let's add them
        # to the graph to keep checking.
        graph[src].add(dest)
        graph[dest].add(src)
    
    # if we've gone through all edges 
    # and found no cycles, return an empty list.
    return []