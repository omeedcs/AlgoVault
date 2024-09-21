def longestSubstringWithoutDups(self, s):
    # contiguous sequence
    if not s:
        return 0

    char_index = {}
    longest = 0
    left = 0
    for right in range(len(s)):
        char = s[right]
        if char in char_index:
            start = char_index[char] + 1
        else:
            # window size calculation is the below formula.
            longest = max(longest, right - left + 1)

        char_index[char] = right
    return longest
