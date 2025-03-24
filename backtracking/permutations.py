# we want to find all permutations 
def permutations(nums):
    result = []
    def backtrack(perm):
        # base case
        if len(perm) == len(nums):
            result.append(perm.copy())
            return

        for num in nums:
            if num in perm:
                perm.append(num)
                backtrack(perm)
                perm.pop()
    backtrack([])
    return result
        


        
        