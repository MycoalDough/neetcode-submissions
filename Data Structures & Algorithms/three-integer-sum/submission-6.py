class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        sol = []

        for n in range(len(nums)):
            if n > 0 and nums[n] == nums[n-1]:
                continue

            left = n+1
            right = len(nums) - 1

            while left < right:
                s = nums[n] + nums[left] + nums[right]

                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    sol.append([nums[n], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return sol



        