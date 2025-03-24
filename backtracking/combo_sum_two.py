def comboSumTwo(self, nums, target):
    # core idea behind this is that we have to 
    # have unique combinations and we can only 
    # use numbers one. 
    # NLOGN sorting. two branches at every step.
    # we end up with the N * 2^N. 
    result = []
    nums.sort() 
    def dfs(i, subset, total):

        if total == target:
            result.append(subset.copy()) 
            return
        
        if total > target or i == len(nums):
            return

        # include 
        subset.append(nums[i])

        # we do +1 because the problem tells us 
        # that we can not reuse a number.
        dfs(i + 1, subset, total + nums[i])
        # if we can reuse a number...
        # dfs(i, subset, total) is sufficient. 

        # once dfs is complete, we want to do 
        # cur.pop()
        subset.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        dfs(i + 1, subset, total)
    dfs(0, [], 0)
    return result
