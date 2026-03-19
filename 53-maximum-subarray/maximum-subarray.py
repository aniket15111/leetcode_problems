class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=nums[0]
        sumi=0
        for i in range(0,len(nums)):
            if (nums[i]<0 and sumi==0) or (sumi+nums[i])<0:
                maxi=max(maxi,nums[i])
                sumi=0
            else:
                sumi+=nums[i]
                maxi=max(sumi,maxi)

            
        return maxi
