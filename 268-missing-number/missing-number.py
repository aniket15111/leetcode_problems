class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total=sum(nums)
        requried_sum=max(nums)*(max(nums)+1)//2
        missing=requried_sum-total
        if missing<=0 and 0  in nums:
            return max(nums)+1
        return missing