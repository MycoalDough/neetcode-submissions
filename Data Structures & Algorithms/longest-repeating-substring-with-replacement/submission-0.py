class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts = {}
        mfreq = 0
        result = 0

        for right in range(len(s)):
            char = s[right]
            counts[char] = counts.get(char, 0) + 1
            mfreq = max(mfreq, counts[char])

            while (right - left + 1) - mfreq > k:
                char_l = s[left]
                counts[char_l] = counts.get(char_l, 0) - 1
                left += 1
            
            result = max(result, right-left+1)

        return result