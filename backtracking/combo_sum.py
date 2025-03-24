# array of distinct or UNIQUE ints. 
# we have a target value.
# we want to return ALL UNIQUE COMBOS
# where the chosen numbers SUM to target.

# the same number can be chosen an UNLIMITED number of times.

def comboSum(nums, target):
    result = []
    def backtrack(i, combo, total):
        # we want to add to the list.
        if total == target:
            result.append(combo.copy())
            return
        
        if i >= len(nums) or total > target:
            # we reached a base case.
            # this combo that we have can not work.
            return

        # finished the base cases.
        # in recursion, what do we want to do 
        # at every step.

        # include the number, which enables reuse.
        combo.append(nums[i])
        backtrack(i, combo, total + nums[i])

        combo.pop()
        # skip the current number and go to the next index. 
        backtrack(i + 1, combo, total)
    backtrack(0, [], 0)
    return result


            
