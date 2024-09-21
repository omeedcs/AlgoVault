def subsets(nums):
    # given some array of unique integers,
    # we return all the possible subsets 
    # of nums.
    # solution can not contain duplicate subsets. 
    
    result = []
    def backtrack(i, subset):
        # base case, has the subset length 
        # exceeded what is possible?
        if i >= len(nums):
            result.append(subset.copy())
            return

        subset.append(nums[i]) # add the current num
        # [1, 2, 3] 
        # pop, backtrack. 
        # call recursive backtracking on the next element
        backtrack(i + 1, subset)
        subset.pop()
        backtrack(i + 1, subset)
    
    backtrack(0, [])
    return result