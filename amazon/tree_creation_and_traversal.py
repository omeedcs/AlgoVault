from collections import deque
class TreeNode: 
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    # construct the tree from a list of values, where None represents empty node.
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root]) 
    
    i = 1 
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] != None:
            node.left = TreeNode(values[i]) 
            queue.append(node.left)
        i += 1 
    
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root



# recurse through the tree.
def dfs(root):
    def pre_order(node, result):
        if not node: 
            return 
        # base case

        result.append(node.val)
        pre_order(node.left, result)
        pre_order(node.right, result) 



"""
    Let's say hypothetically we wanted to do this for an N-ARY tree.
"""

class TreeNode:
    def _init__(self, val = 0, children = None):
        self.val = val
        self.children = children if children else []

# values = [[value, # of children], []].. etc
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0][0])
    queue = deque([(root, values[0][1])])
    i = 1

    while queue and i < len(values):
        parent, num_children = queue.popleft()
        for _ in range(num_children):
            if i < len(values):
                child = TreeNode(values[i][0])
                parent.children.append(child)
                queue.append((child, values[i][1]))
                i += 1
    return root

def dfs(root):
    def preorder(node, result):
        if not node:
            return
        
        result.append(node.val)
        for child in node.children:
            preorder(child, result)
    result = []
    preorder(root, result)
    return result
        