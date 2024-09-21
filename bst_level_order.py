import collections
def levelOrderTraversal(self, root):
    queue = collections.deque()
    traversal = []
    
    # edge case, do we even have a root node?
    if root:
        queue.append(root)
        # remember, we need to have a root 
        # to even be able to traverse.
    
    while queue:
        level = [] 
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        traversal.append(level)
    return traversal
