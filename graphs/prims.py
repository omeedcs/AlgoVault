import heapq

def prim_mst(n, edges):
    # Build the graph as an adjacency list
    graph = {i: [] for i in range(n)}
    for src, dest, weight in edges:
        graph[src].append((weight, dest))
        graph[dest].append((weight, src))  # Since the graph is undirected

    # Initialize the MST variables
    total_cost = 0
    mst_edges = []
    visited = set()

    # Use a min-heap to select the edge with the minimum weight
    min_heap = []

    # Start from node 0 (arbitrary choice)
    start_node = 0
    visited.add(start_node)
    for weight, neighbor in graph[start_node]:
        heapq.heappush(min_heap, (weight, start_node, neighbor))

    # Continue until we include all nodes in the MST
    while min_heap and len(visited) < n:
        # Pop the edge with the smallest weight
        weight, src, dest = heapq.heappop(min_heap)
        if dest not in visited:
            # Include the node in the MST
            visited.add(dest)
            mst_edges.append((src, dest, weight))
            total_cost += weight

            # Add all edges from the new node to the heap
            for next_weight, neighbor in graph[dest]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (next_weight, dest, neighbor))

    # Check if all nodes are included in the MST
    if len(visited) != n:
        return None  # The graph is not connected

    return mst_edges, total_cost

# Example usage
if __name__ == "__main__":
    n = 5  # Number of nodes
    edges = [
        (0, 1, 2),
        (0, 3, 6),
        (1, 2, 3),
        (1, 3, 8),
        (1, 4, 5),
        (2, 4, 7),
        (3, 4, 9)
    ]

    mst, cost = prim_mst(n, edges)
    if mst is not None:
        print("Minimum Spanning Tree edges:")
        for src, dest, weight in mst:
            print(f"{src} -- {dest} (Weight: {weight})")
        print(f"Total cost of MST: {cost}")
    else:
        print("The graph is not connected, and an MST cannot be formed.")


# Dijkstras: to find shortest path between a single source 
# node and all other nodes in a graph. Useful for routing
# and navigation problems.

# Minimum Spanning Tree (MST): connect all the vertices in the 
# graph using least possible total edge weight. 
# when you return a list of MSTs, the list represents the set 
# of edges that connect all vertices in the graph, have minimum 
# total weight, and do NOT form any cycles. 
#