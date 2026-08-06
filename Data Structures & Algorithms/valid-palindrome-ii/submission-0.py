class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        used = False

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1

            elif s[left+1] == s[right] and used == False:
                left += 2
                right -= 1 
                used = True
            
            elif s[right-1] == s[left] and used == False:
                left += 1
                right -= 2
                used = True
            
            else:
                return False
            
        return True

            