class Solution:
    def upperBound(self, arr, target):
        i=0
        j=len(arr)-1
        ans=len(arr)
        while i<=j:
            mid=(i+j)//2
            if arr[mid]>target:
               ans=mid
               j=mid-1
            else:
                i=mid+1
               
            
        return ans
        