class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        big1, big2, small1, small2 = float('-inf'), float('-inf'), float('inf'), float('inf')

        for n in nums:
            if n > big1:
                big2 = big1
                big1 = n
            elif n > big2:
                big2 = n
            
            if n < small1:
                small2 = small1
                small1 = n
            elif n < small2:
                small2 = n
        
        return big1 * big2 - small1 * small2