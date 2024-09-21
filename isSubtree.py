def isSubtree(self, root, subRoot):
    def same(root, subRoot):
        if not root and not subRoot:
            return True # base case. 
        if root and subRoot and root.val == subRoot.val:
            # same logic as the tree matching.
            return same(root.left, subRoot.left) and same(root.right, subRoot.right)
        else:
            return False

    if not root and not subRoot: 
        return True 

    # exhausted the main tree with no match in the subtree.
    if not root and subRoot:
        return False
    
    if same(root, subRoot):
        return True

    # we just need a match on one of the subtrees.
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)