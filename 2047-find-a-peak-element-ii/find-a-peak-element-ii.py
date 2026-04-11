class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        i=0
        j=m-1

        while i<=j:
            mid=(i+j)//2
            row=self.maxelement(mat,n,mid)
            left=mat[row][mid-1] if mid>0 else -1
            right=mat[row][mid+1] if mid<m-1 else -1
            if mat[row][mid]> left and mat[row][mid]>right:
                return [row,mid]

            elif mat[row][mid]<left: j=mid-1
            else: i=mid+1

        return [-1,-1]

        
    def maxelement(self,mat,n,mid):
        max_val=-1
        index=-1
        for i in range(n):
            if mat[i][mid] > max_val:
                max_val = mat[i][mid]
                index = i
        return index