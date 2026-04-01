#User function Template for python3
class Solution:
    def findCeil(self, arr, x):
        i=0
        j=len(arr)-1
        ans=-1
        while i<=j:
            mid=(i+j)//2
            if arr[mid]>=x:
                j=mid-1
                ans=mid
            else:
                i=mid+1
                
                
                
        return ans
