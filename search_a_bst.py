# we are recursing a binary search tree.
def search(root, target):
    # base case, we never found target.
    # ensures that the recursion effectively terminates.
    if not root:
        return False

    if target > root.val: 
        search(root.right, target)
    elif target < root.val:
        search(root.left, target)
    else:
        return True # we found the target.

