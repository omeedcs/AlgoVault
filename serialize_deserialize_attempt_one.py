# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # what if we do a in-order and pre-order traversal, then split 
        # the string, reconstruct it into an array in deserialize,
        # and then recursively build the tree back up using a previous
        # technique we learned.

        # in order: left -> root -> right
        # pre order: root -> left -> right
        preord = []
        inord = []
        
        def preorder(root):
            if not root:
                return
            
            preord.append(root.val)
            preorder(root.left)
            preorder(root.right)

        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            inord.append(root.val)
            inorder(root.right)
        
        preorder(root)
        inorder(root)
        preorder_str = ','.join(map(str, preord))
        inorder_str = ','.join(map(str, inord))
        serialized = preorder_str + "#" + inorder_str
        return serialized

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        result = data.split("#")
        preorder_str, inorder_str = data.split("#")
        preorder = list(map(int, preorder_str.split(','))) if preorder_str else []
        inorder = list(map(int, inorder_str.split(','))) if inorder_str else []
        print(preorder)
        print(inorder)

        def buildTree(preorder, inorder):
            # remember that the mid point in an inorder list is going to be
            # the split point, basically where the root is.
            if not preorder or not inorder:
                return None
            mid = inorder.index(preorder[0])
            root = TreeNode(preorder[0])
            root.left = buildTree(preorder[1: mid + 1], inorder[:mid + 1])
            root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])
            return root
        
        result = buildTree(preorder, inorder)
        return result


