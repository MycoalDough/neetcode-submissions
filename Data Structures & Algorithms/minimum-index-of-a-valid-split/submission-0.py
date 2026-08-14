class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dom_num = 0
        save = {}

        for n in nums:
            save[n] = save.get(n, 0) + 1
        
        dom_num = max(save, key=save.get)
        total_dom = save[dom_num]
        left_dom = 0

        for i in range(len(nums)-1):
            if nums[i] == dom_num:
                left_dom += 1

            left_size = i+1
            right_size = len(nums)-left_size
            right_dom_freq = total_dom - left_dom

            if left_dom * 2 > left_size and right_dom_freq * 2 > right_size:
                return i

        return -1

