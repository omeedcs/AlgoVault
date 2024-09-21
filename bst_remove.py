def remove(root, val):
    # recursive base case. 
    if not root:
        return None
    
    # well first, we need to find the value
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        # ok. we got a match. lets check, are we missing left child or right child?
        # this is for the next step of the recursion. Think about it, we want to 
        # set proper references for our children as we actually remove the node 
        # and attempt to maintain the property of the binary search tree.
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            # ok.
            minNode = minimumValueInTree(root.right) # use the function we know that works.
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
        return root
    