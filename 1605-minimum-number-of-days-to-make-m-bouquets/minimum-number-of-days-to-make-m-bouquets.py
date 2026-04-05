class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        i=min(bloomDay)
        j=max(bloomDay)
        main=-1

        while i<=j:
            mid=(i+j)//2
            if self.fun(bloomDay,mid,m,k):
                main=mid
                j=mid-1
                
            else:
                i=mid+1
        return main


    def fun(Self,arr,mid,m,k):
        count=0
        ans_count=0
        for i in arr:
            if i<=mid:
                count+=1
                if count==k:
                    ans_count+=1
                    count=0
            else:
                count=0
            
            if ans_count>=m:
                return True
        return False
