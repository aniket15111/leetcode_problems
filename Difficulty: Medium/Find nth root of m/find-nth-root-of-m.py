class Solution:
    def nthRoot(self, n, m):
       i=1
       j=m
       if m == 1: return 1
       if m == 0: return 0       
       while i<=j:
           mid=(i+j)//2
           prod=1
           prod = pow(mid, n)
           if prod==m:
              return mid
           elif prod<m:
              i=mid+1
           else:
              j=mid-1
       return -1
               
       
