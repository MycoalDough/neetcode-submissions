class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = []
        m = 0

        for c in s:
            if c not in check:
                check.append(c)
            else:
                check.append(c)
                while c in check:
                    check.pop(0)

            m = max(len(check), m)

        return max(len(check),m)
        