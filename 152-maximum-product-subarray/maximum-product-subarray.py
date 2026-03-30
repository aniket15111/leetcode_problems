class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix=1
        ss=1
        sufix=float(-inf)
        j=len(nums)-1
        for i in range(0,len(nums)):
            prefix*=nums[i]
            ss*=nums[j]
            j-=1
            sufix=max(sufix,prefix,ss)
            if prefix==0:
                prefix=1
            if ss==0:
                ss=1
        return sufix