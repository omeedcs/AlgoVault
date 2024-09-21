def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    
    return prefix

# Example usage
arr = [1, 2, 3, 4, 5]
result = prefix_sum(arr)
print(result)  # Output: [1, 3, 6, 10, 15]

def range_sum_queries(arr, queries):
    # Calculate prefix sum
    prefix = prefix_sum(arr)
    
    # Process queries
    results = []
    for L, R in queries:
        if L == 0:
            results.append(prefix[R])
        else:
            results.append(prefix[R] - prefix[L-1])
    
    return results

# Example usage
arr = [1, 2, 3, 4, 5]
queries = [(1, 3), (2, 4), (0, 2)]
result = range_sum_queries(arr, queries)
print(result)  # Output: [9, 12, 6]