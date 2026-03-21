class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        row_mark=[0]*n
        col_mark=[0]*m

        for row in range(n):
            for col in range(m):
                if matrix[row][col]==0:
                    row_mark[row]=1
                    col_mark[col]=1

        for row in range(n):
            for col in range(m):
                if row_mark[row]==1 or col_mark[col]==1:
                    matrix[row][col]=0