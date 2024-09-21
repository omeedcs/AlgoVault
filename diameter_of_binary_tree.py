def diameterOfBinaryTree(self, root):
    longestPath = 0 

    def dfs(root):
        nonlocal longestPath

        if not root:
            return 0
        
        # this is a post-order traversal.
        left = dfs(root.left)
        right = dfs(root.right)

        longestPath = max(longestPath, left + right)
        return 1 + max(left, right) # this accounts for the current
        # node when returning up to the parent.
    

