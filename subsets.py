def subsets(nums):
    # given some array of unique integers,
    # we return all the possible subsets 
    # of nums.
    # solution can not contain duplicate subsets. 
    
    result = []
    def backtrack(i, subset):
        # base case, has the subset length 
        # exceeded what is possible?
        res.append(subset.copy())
        return

        subset.append(nums[i])
        backtrack(i + 1, subset)
        subset.pop()
        backtrack(i + 1, subset)
    
    backtrack(0, [])
    return res