from collections import deque

def bfs_shortest_path(adj_list, start, goal):
    """
    Finds the shortest path in an unweighted graph using BFS.

    Parameters:
    adj_list (dict): Adjacency list representing the graph.
                     Keys are nodes, values are lists of neighboring nodes.
    start (any): The source node.
    goal (any): The destination node.

    Returns:
    list: A list of nodes representing the shortest path from start to goal.
          Returns an empty list if no path exists.
    """
    # Edge case: if the start and goal are the same
    if start == goal:
        return [start]

    visited = set()
    queue = deque()
    predecessor = dict()

    # Initialize BFS
    visited.add(start)
    queue.append(start)
    predecessor[start] = None

    while queue:
        current_node = queue.popleft()

        # Explore neighbors
        for neighbor in adj_list.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                predecessor[neighbor] = current_node
                queue.append(neighbor)

                # Early termination if the goal is found
                if neighbor == goal:
                    # Reconstruct the path
                    path = []
                    cur = goal
                    while cur is not None:
                        path.append(cur)
                        cur = predecessor[cur]
                    path.reverse()
                    return path

    # If the goal was not reached
    return []

# Example usage:
if __name__ == "__main__":
    # Sample graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = 'A'
    goal_node = 'F'
    path = bfs_shortest_path(graph, start_node, goal_node)
    if path:
        print(f"Shortest path from {start_node} to {goal_node}: {' -> '.join(path)}")
    else:
        print(f"No path exists from {start_node} to {goal_node}")
