class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        highest = 0

        while left < right:
            t = min(heights[left], heights[right])
            t = t * (right-left)

            if t > highest:
                highest = t

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return highest
