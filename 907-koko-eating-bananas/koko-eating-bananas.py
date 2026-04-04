class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i=1
        j=max(piles)
        res=j
        while i<=j:
            mid=(i+j)//2
            val=self.fun(piles,mid)
            if val<=h:
                res=mid
                j=mid-1
            else:
                i=mid+1
        return res


    def fun(self,arr,mid):
        total=0
        for i in arr:
            total += (i + mid - 1) // mid
        return total