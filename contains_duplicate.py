# find a duplicate element in an array.

def hasDuplicate(nums) -> bool:
    occurences = {}
    for num in nums:
        if num in occurences:
            return True
        else:
            occurences[num] = 1
    return False