def minInBST(root):
    curr = root
    # this is simple because of the property of a binary search tree.
    while curr and curr.left:
        curr = curr.left
    return curr