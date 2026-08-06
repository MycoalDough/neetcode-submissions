class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen_s = set()
        seen_t = set()
        for i in range(len(s)):
            seen_s.add(s[i])
            seen_t.add(t[i])

        return seen_s == seen_t