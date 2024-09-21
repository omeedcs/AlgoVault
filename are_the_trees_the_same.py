def areTheTreesTheSame(self, p, q):
    def dfs(p, q):
        if not p and not q:
            # base case
            return True
        if p and q and p.val == q.val:
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)
            return left
        else:
            # if we got here, then the subtrees did not match.
            return False
