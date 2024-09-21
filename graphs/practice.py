import collections

def scoreUserKeystrokes(userInput): 

    # validate user input
    if not userInput:
        return 0
    DIRECTIONS = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    keyboard = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'],
    ]

    def find_char(char):
        for i, row in enumerate(keyboard): 
            if char in row:
                return i, row.index(char)
        return None

    def bfs(start, goal):
        queue = collections.deque()
        queue.append((start, 0))
        visited = set()
        visited.add(start)
        while queue:
            (row, col), dist = queue.popleft()
            if keyboard[row][col] == goal: 
                return dist
        # queue is < Node in 2D Matrix, Distance >
        # distance being the distance it is taking to 
        # get from the current node to the goal node, 
        # which the new character in our input.
        for direction in DIRECTIONS: 
            x, y = direction
            nx = row + x
            ny = row + y
            # implement wraparound 
            nx = nx % len(keyboard)
            ny = ny % len(keyboard[0])
            # this works because when you divide a number N using modulu, it is always going to be in the range of 0 to N-1. 
            # this naturally creates a "WRAP" back into the valid range of indices. 
            # this is used in circular data structures. 
            # this is also used in game worlds, for example when pacman moves off 
            # one side of the screen to appear onto the other side of the screen.
            if (nx, ny) not in visited:
                queue.append((nx, ny), dist + 1)
                visited.add((nx, ny))
        return -1 # no distance.

    total_score = 0
    # think about this.
    # you want a start node. That start node is 
    # the first position in your string. 
    # you also want a goal node, which is technically
    # the ith index after the user input of 0. 
    # the idea is we keep shifting our start post and 
    # our goal post, doing traversals, and keeping track
    # of the total values to know what the keystrokes
    # actually are going to be.
    prev_pos = find_char(userInput[0])

    for char in userInput[1:]: #skip the first index
        # kind of a work around to enumerate
        goal_pos = find_char(char)
        if prev_pos and goal_pos:
            total_score += bfs(prev_pos, char)
            # remember, the bfs is returning a distance.
            prev_pos = goal_pos
        else: 
            # based on the description, this is likely 
            # never going to happen, because the user is 
            # basically bounded by what is allowed on the 
            # screen when they are doing the actual keystrokes.
            "Invalid Character in Password"
    return total_score
        



