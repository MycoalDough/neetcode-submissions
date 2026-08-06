class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        l = set(s)
        r = set(t)

        return l == r