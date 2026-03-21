class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        # row_mark=[0]*n      matrix[row][0]
        # col_mark=[0]*m      matrix[0][col]
        col0=1
        for row in range(n):
            for col in range(m):
                if matrix[row][col]==0:
                    matrix[row][0]=0
                    if col!=0:
                        matrix[0][col]=0
                    else:
                        col0=0

        for row in range(1,n):
            for col in range(1,m):
                if matrix[row][0]==0 or matrix[0][col]==0: 
                    matrix[row][col]=0
        
        if matrix[0][0]==0:
            for i in range(m):
                matrix[0][i]=0
        if col0==0:
            for i in range(n):
                matrix[i][0]=0

        