class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumi = nums[0]
        maxi = nums[0]

        for i in range(1, len(nums)):
            sumi = max(nums[i], sumi + nums[i])
            maxi = max(maxi, sumi)

        return maxi