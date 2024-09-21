def goodNodes(self, root):
    def dfs(node, maxVal):
        if not node:
            return 0 # base case 
        
        if node.val >= maxVal: 
            result = 1
        else: 
            result = 0
        
        maxVal = max(maxVal, node.val)
        result += dfs(node.left, maxVal)
        result += dfs(node.right, maxVal)
        return result

# the property of a good node is that the node is considered good
# if the path from the root of the tree to that node contains
# no nodes with a value that is greater than the value of that
# current node in the tree.

# the best way to think about this is that ok, if we get to a leaf,
# then the value is obviously going to be 0. 
# remember that a base case is basically the simplest case.

# then we check to see if the current nodes value is greater than
# the maximumValue that we are keeping track of.
# maxValue is the maximum value that we have seen SO FAR.
# technically, this means that we can count the node as GOOD.
# GOOD -> 1
# NOT GOOD -> 0

# as we traverse down, compare the current nodes va;lue to the 
# maximum value that currently is being tracked.

# then, we call dfs on the right and left children, and keep 
# passing the updated maximum value as we go deeper into the tree.
# we continue to sum up the good nodes we find in the tree 
# as we actually move deeper into the tree.