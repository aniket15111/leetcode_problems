class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        i=max(nums)
        j=sum(nums)
        ans=0
        while i<=j:
            mid=(i+j)//2

            if self.fun(nums,mid,k):
                ans=mid
                j=mid-1
            else:
                i=mid+1
        return ans



    def fun(self,nums,mid,k):
        count=1
        sumi=0
        for i in nums:
            if i+sumi>mid:
                sumi=i
                count+=1
            else:
                sumi+=i
        return count<=k

            
                
