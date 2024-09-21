from collections import deque
def rightSide(self, root):
    queue = deque()
    result = []
    queue.append(root)
    while queue:
        # iterate over level
        for _ in range(len(queue)):
            node = queue.popleft()
            if node:
                right = None
                queue.append(node.left)
                queue.append(node.right)
        if right:
            # this allows us to get the rightmost node .
            result.append(node.val)
    return result
    