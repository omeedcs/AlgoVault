def findMin(nums):
    start = 0 
    end = len(nums) - 1
    curr_min = float("-inf")
    while start < end:
        mid = start + (end - start) // 2
        curr_min = min(curr_min, nums[mid])
        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid
