import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # implement djikstras shortest path algorithm.
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for sr, dest, weight in edges:
            graph[sr].append((dest, weight))
            # only a one way direction
        
        shortest = {} # < Node, CostToNode>
        minHeap = [] # < cost, Node> 
        # if src not in graph:
        # do we handle the slight edge case in which a source does not exist in the graph?
        minHeap.append((0, src))

        while minHeap:
            # pop off the heap
            cost, node = heapq.heappop(minHeap)
            if node in shortest:
                continue
            else:
                shortest[node] = cost
                
                for nei, neiCost in graph[node]:
                    if nei in shortest:
                        continue
                    else:
                        heapq.heappush(minHeap, (neiCost + cost, nei))
        # if it is unreachable, unreachable vertices should be marked with -1 
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest





