class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(r):
            return False
            
        l = set(s)
        r = set(t)

        return l == r