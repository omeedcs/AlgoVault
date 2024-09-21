def maxDepth(self, root):
    if not root:
        return 
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))