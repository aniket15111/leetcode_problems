class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        ans=-1
        prev=nums[0]
        for i in nums:
            sub=i-prev
            ans=max(ans,sub)
            prev=i
        return ans
        
