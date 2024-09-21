def canReachLeaf(root):
    if not root or root.val:
        return False # let the parent know we failed. base case.

    if not root.left and not root.right:
        return True # we made it to a leaf node.

    if canReachLeaf(root.left):
        return True
    if canReachLeaf(root.right):
        return True
    
    return False

# now what if we want to access that path we just found?
def leafPath(root, path):
    if not root or not root.val:
        return False
    path.append(root.val)
    if not root.left and not root.right:
        return True 
    if leafPath(root.left, path):
        return True
    if leafPath(root.right, path):
        return True
    path.pop() # pop back up to the parent.
    return False