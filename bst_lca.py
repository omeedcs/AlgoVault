# iterative tree style.
def lca(self, root, p, q):
    cur = root
    if p.val > cur.val and q.val > cur.val:
        cur = cur.right
    elif p.val < cur.val and q.val < cur.val:
        cur = cur.left
    else:
        return cur
    
# (all left descendents) <= currentNode < (all right descendents)
# if you set a cur reference to the root,
# the traversal basically becomes trivial.