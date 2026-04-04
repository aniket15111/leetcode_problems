class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        n=len(arr)
        i=1
        j=n-2
        
        if n==1: return 0
        if arr[0]>arr[1]: return 0
        if arr[n-1]>arr[n-2]: return n-1

        while i<=j:
            mid=(i+j)//2

            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid+1]>arr[mid]:
                i=mid+1
            else:
                j=mid-1
        return i