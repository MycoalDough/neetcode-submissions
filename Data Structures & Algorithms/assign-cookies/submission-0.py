class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        for child in g:
            for i in range(len(s)):
                if child <= s[i]:
                    res += 1
                    s.pop(0)
                    break
        
        return res