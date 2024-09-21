def permutations(self, nums): 
    perms = []
    def backtracking(perm):
        if len(perm) == len(nums):
            perms.append(perm.copy())
            return
        
        for num in nums:
            if num not in perm:
                perm.append(num)
                backtracking(perm)
                perm.pop() # try a new path.

