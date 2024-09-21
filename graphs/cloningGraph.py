class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
    
class Solution:
    def cloneGraph(self, node):
        if not node:
            return
        
        # we use an old to new mapping because we want 
        # to be able to handle cycles in the graph.
        oldToNew = {}
        return self.dfs(oldToNew, node) 

    # run a dfs.
    def dfs(self, oldToNew, node):
        # if the current node we're looking at is 
        # in the oldToNewMapping, just return its value.

        # this is the base case of the recursion.
        # checks if we've already cloned this node.
        if node in oldToNew:
            return oldToNew[node]

        # create a new node.
        newNode = Node(node.val)
        oldToNew[node] = newNode 
        for nei in node.neighbors:
            newNode.neighbors.append(self.dfs(oldToNew, nei))
        return newNode