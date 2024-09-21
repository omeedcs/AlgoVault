class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
    
class BurgerKing:
    def cloneGraph(self, node):
        if not node:
            return
        
        oldToNew = {}
        return self.dfs(oldToNew, node) 

    def dfs(self, oldToNew, node):
        if node in oldToNew:
            return oldToNew[node]

        newNode = Node(node.val)
        oldToNew[node] = newNode 
        for nei in node.neighbors:
            newNode.neighbors.append(self.dfs(oldToNew, n))
        return newNode