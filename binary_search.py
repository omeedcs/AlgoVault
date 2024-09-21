def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low) + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


def sqrt(x):
    low = 0
    high = x
    while low <= high:
        mid = (low) + (high - low) // 2
        if mid * mid < x:
            low = mid + 1
        elif mid * mid > x:
            high = mid - 1
        else:
            return mid
    return high
            
        