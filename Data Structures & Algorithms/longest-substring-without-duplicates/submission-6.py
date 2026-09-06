class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        left = 0
        max_len = 0
        
        for right, c in enumerate(s):
            if c in chars and chars[c] >= left:
                left = chars[c] + 1
            chars[c] = right
            max_len = max(max_len, right-left+1)

        return max_len

            