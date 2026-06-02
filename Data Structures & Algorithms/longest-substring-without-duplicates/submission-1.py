class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = 0
        seen = {}

        for r, char in enumerate(s):
            if char in seen and seen[char] >= l:
                l = seen[char] + 1

            seen[char] = r
            max_len = max(max_len, r-l + 1)

        return max_len




        

        

        


