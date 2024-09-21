from collections import deque

def rightSideView(self, root):
    result = []
    queue = deque()
    while queue:
        right = None
        for i in range(len(queue)):
            node = queue.popleft()
            # does the node exist?
            if node:
                right = node
                queue.append(node.left)
                queue.append(node.right)
        if right:
            result.append(right.val)
    return result



# basically, we want to make sure that the right
