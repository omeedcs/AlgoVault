# iteratively inserts each element of an unsorted list into its correct position
# in a sorted portion of the list.

# Function to perform insertion sort on an array
def insertion_sort(arr):
    # Get the length of the array
    n = len(arr)
    
    # If the array has 1 or fewer elements, it's already sorted, so return
    if n <= 1:
        return
    else:
        # Iterate through the array starting from the second element (index 1)
        for i in range(1, n):
            # Store the current element as the key to be inserted
            key = arr[i]
            
            # Initialize j as the index immediately before i
            j = i - 1
            
            # Move elements of arr[0..i-1] that are greater than key
            # to one position ahead of their current position
            while j >= 0 and key <= arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            
            # Place the key in its correct position in the sorted subarray
            arr[j + 1] = key