def recursive_binary_search(arr, target, low, high):
    # Base case: if the search space is empty, the target is not in the array
    if low > high:
        return -1
    
    # Calculate the middle index
    mid = (low + high) // 2
    
    # If the middle element is the target, return its index
    if arr[mid] == target:
        return mid
    
    # If the target is less than the middle element, search the left half
    elif target < arr[mid]:
        return recursive_binary_search(arr, target, low, mid - 1)
    
    # If the target is greater than the middle element, search the right half
    else:
        return recursive_binary_search(arr, target, mid + 1, high)

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 7
result = recursive_binary_search(arr, target, 0, len(arr) - 1)
print(f"Target {target} found at index: {result}")