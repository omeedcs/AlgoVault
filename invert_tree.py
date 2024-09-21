def invertBinaryTree(self, root):
    if not root:
        return None

    temp = root.left
    root.left = root.right
    root.right = temp
    self.invertBinaryTree(root.left)   
    self.invertBinaryTree(root.right)
    return root