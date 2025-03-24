def subsetsTwo(nums):
    # this may contain duplicates. not all 
    # numbers are unique.
    # return all possible subsets. 
    # but, we can not contain duplicate subsets.
    result = []
    nums.sort() # to make sure dups are adjacent.
    def backtrack(i, subset):
        # base case.
        if i == len(nums):
            result.append(subset.copy())
            return
        
        # takes care of 
        # all subsets that include THIS number. 
        subset.append(nums[i])
        backtrack(i + 1, subset) 

        # before generating all subsets 
        # that do not include THIS number... 
        # we should remove from the subset 
        # the value that we just added to it.
        subset.pop() # will pop the value we just added from the append. 
        # skip dups
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        
        backtrack(i + 1, subset)

    backtrack(0, [])
    return result


