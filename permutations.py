def permutations(self, nums):
    perms = []
    perm = []
    backtrack(perms, perm, nums)

    def backtrack(perms, perm, nums):
        if len(perm) == len(nums):
            perms.append(perm.copy())
            return

        for num in nums:
            if num not in perm:
                # By appending the number before the recursive call, we are building up the permutation.
                perm.append(num)
                backtrack(perms, perm, nums)
                # After exploring that path fully, we remove the number (with pop()) to go back and try a different one.
                perm.pop()