def binary_search_2d(matrix):
    top = 0
    bottom = len(grid) - 1
    while top <= bottom:
        mid = (top) + (bottom - top) // 2
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            # run a binary search on row.
            break
        elif matrix[mid][0] > target:
            bottom = mid - 1
        else:
            top = mid + 1

def binary_search(mid, target):
    pass