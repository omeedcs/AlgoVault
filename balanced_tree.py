def isTreeBalanced(self, root) -> bool: 
    def dfs(root):
        if not root:
            return [True, 0]
        
        left = dfs(root.left)
        right = dfs(root.right)
        balanced = False
        # we are checking the property that the problem description
        # specified, the balanced property is from the far right 
        # of the conditional.
        if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
            balanced = True
        heightOfTree = max(left[1], right[1]) + 1
        return [balanced, heightOfTree] # return information back up to the parent.
    
    result = dfs(root)
    return result[0]
