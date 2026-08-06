class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        sol = []

        for n in range(len(nums)):
            left = n+1
            right = len(nums) - 1

            while left < right:
                s = nums[n] + nums[left] + nums[right]

                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    if not [nums[n], nums[left], nums[right]] in sol:
                        sol.append([nums[n], nums[left], nums[right]])
                    left += 1
                    right -= 1

        return sol



        