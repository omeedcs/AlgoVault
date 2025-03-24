# if you have an array of numbers that are UNIQUE. 
# lets say we want to return ALL the possible subsets. 
# no duplicate subsets. 
# solution can be in any order.

# Recursive Backtracking #1:

def subsets(nums):
    res = [] # classic method 
    def backtrack(i, curSubset):
        if i >= len(nums):
            res.append(curSubset.copy())
            return
        
        # include the current element during exploration
        curSubset.append(nums[i])
        backtrack(i + 1, curSubset)


        # dont include the current element during exploration
        curSubset.pop()
        backtrack(i + 1, curSubset)

    backtrack(0, [])
    return res

