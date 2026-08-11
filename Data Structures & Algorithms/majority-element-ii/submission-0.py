class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ret = []

        l = {}

        for n in nums:
            l[n] = l.get(n, 0) + 1

        
        for n in l:
            if l[n] > math.floor(len(nums)/3):
                ret.append(n)

        return ret