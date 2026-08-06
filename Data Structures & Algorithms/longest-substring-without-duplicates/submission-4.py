class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        m = 0

        for c in s:
            if c not in check:
                check.append(c)
            else:
                while c in check:
                    check.pop(0)
                check.append(c)


            m = max(len(check), m)

        return max(len(check),m)
        