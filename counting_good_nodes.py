def goodNodes(self, root):
    def dfs(node, maxVal):
        # base case 
        if not node:
            return 0

        if node.val >= maxVal:
            result = 1
        else:
            result = 0
        
        maxVal = max(maxVal, node.val)
        result += dfs(node.left, maxVal)

