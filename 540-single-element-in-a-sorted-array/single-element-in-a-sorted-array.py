class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        i,j=1,len(arr)-2
        n = len(arr)
        if n == 1: return arr[0]
        if arr[0] != arr[1]: return arr[0]
        if arr[n-1] != arr[n-2]: return arr[n-1]
        while i<=j:
            mid=(i+j)//2
            if arr[mid]!=arr[mid+1] and arr[mid]!=arr[mid-1]:
                return arr[mid]
           
            if (mid%2==0 and arr[mid]== arr[mid+1]) or (mid%2==1 and arr[mid]==arr[mid-1]):
                i=mid+1
            else:
                j=mid-1