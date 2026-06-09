class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mini=nums[0]
        maxi=-1
        for i in nums:
            mini=min(i,mini)
            maxi=max(i,maxi)
        
        return (maxi-mini)*k