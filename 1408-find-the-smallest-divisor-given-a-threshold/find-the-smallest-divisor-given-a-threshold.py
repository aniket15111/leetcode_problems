class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        i = 1
        j = max(nums)
        ans=0
        while i<=j:
            mid=(i+j)//2
            if self.divisor(nums,mid,threshold):
                ans=mid
                j=mid-1
            else:
                i=mid+1
        return ans



    def divisor(self,nums,mid,a):
        dsum=0
        for i in nums:
            dsum+= (i+mid-1)//mid
            if dsum>a:
                return False
        return True
