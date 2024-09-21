def insert(root, target):
    # base case is we made it 
    # to an insertable position. 
    # Think about it, why would we insert 
    # anywhere other than a leaf node, especially 
    # in a tree that is already maintaining the 
    # sorted property?
    if not root:
        return TreeNode(target)
    
    if target > root.val:
        root.right = insert(root.right, target)
    elif target < root.val:
        root.left = insert(root.left, target)
    else:
        return root
    