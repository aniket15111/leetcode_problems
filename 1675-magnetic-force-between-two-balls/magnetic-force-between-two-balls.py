class Solution:
    def maxDistance(self, stalls: List[int], k: int) -> int:
        stalls.sort()
        i=1
        j=stalls[-1]-stalls[0]
        maxi=0
        while i<=j:
            mid=(i+j)//2
            mini=self.fun(stalls,mid,k)
            
            if mini==-1:
                j=mid-1
            else:
                i=mid+1
                maxi=max(maxi,mini)
                
        return maxi
            
            
            
    def fun(self,arr,mid,k):
        prev=0
        mini=float('inf')
        count=1
        for i in range(0,len(arr)):
            if (arr[i]-arr[prev])>=mid:
                mini=min(mini,(arr[i]-arr[prev]))
                prev=i
                count+=1
        
        if count<k:
            return -1
        else:
            return mini
            