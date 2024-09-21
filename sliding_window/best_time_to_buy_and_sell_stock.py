def maxProfit(self, prices):
    left = 0
    maximum = 0
    minimum = prices[left]
    # start at 1 idx. -> classic pattern of left 
    # pointer and right pointer moving slowly.
    for i in range(1, len(prices)):
        prev_day = prices[left]
        cur_day = prices[i]
        if prev_day <= minimum:
            minimum = prev_day
        diff = cur_day - minimum
        if diff >= maximum:
            maximum = diff
        left += 1
    return maximum


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        maximum = 0
        for right in range(len(s)): 
            while s[right] in char_set:
                # as long as there is a duplicate, remove it from left.
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            cur_window_size = right - left + 1
            maximum = max(right - left + 1, maximum)
        return maximum



