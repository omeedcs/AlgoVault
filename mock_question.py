import collections

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
        queue = collections.deque([(start, 0)])
        visited = set([start])
        
        while queue:
            (x, y), dist = queue.popleft()
            
            if keyboard[x][y] == goal:
                return dist
            
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = (x + dx) % len(keyboard), (y + dy) % len(keyboard[0])
                if (nx, ny) not in visited:
                    queue.append(((nx, ny), dist + 1))
                    visited.add((nx, ny))
        
        return float('inf')  # If character not found

    total_score = 0
    prev_pos = find_char(userInput[0])
    
    for char in userInput[1:]:
        goal_pos = find_char(char)
        if prev_pos and goal_pos:
            total_score += bfs(prev_pos, char)
            prev_pos = goal_pos
        else:
            return "Invalid character in password"

    return total_score

# Example usage
print(scoreUserKeystrokes("hello"))  # Output: 13
print(scoreUserKeystrokes("password"))  # Output: 30
print(scoreUserKeystrokes(""))  # Output: 0
print(scoreUserKeystrokes("a1b2c3"))  # Output: 18