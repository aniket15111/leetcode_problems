class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row=len(mat)
        col=len(mat[0])
        row_count = [0] * row
        col_count = [0] * col
        count=0
        for i in range(row):
            for j in range(col):
                if(mat[i][j]==1 ):
                    row_count[i]+=1
                    col_count[j]+=1
        for i in range(row):
            for j in range(col):
                if(mat[i][j]==1 ):
                    if(row_count[i]==1 and col_count[j]==1):
                        count+=1
        return count                 
                    
