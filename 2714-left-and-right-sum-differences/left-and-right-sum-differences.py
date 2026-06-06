class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left=0
        right=0
        sumi=sum(nums)
        ans=[]
        for i in range(len(nums)):
            right=sumi-nums[i]
            sumi-=nums[i]
            ans.append(abs(left-right))
            left+=nums[i]

        return ans
