def scoreUserKeystrokes(userInput):
    if not userInput:
        return 0
    
    keyboard = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
    ]

    def find_char(char):
        for i, row in enumerate(keyboard):
            if char in row: 
                return i, row.index(char)
        return None
    
    def bfs(start, goal): 
        queue = collections.deque()
        visited = set()
        start = userInput[0]
        while queue:
            (x, y), dist = queue.popleft()
            
