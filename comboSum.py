def comboSum(self, nums, target):
    res = []
    def backtrack(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if total > target or i >= len(nums):
            return

        cur.append(nums[i])
        backtrack(i, cur, total + nums[i])
        cur.pop()
        backtrack(i + 1, cur, total)

    backtrack(0, [], 0) 