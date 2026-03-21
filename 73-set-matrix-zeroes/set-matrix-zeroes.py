class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        zeroes=[]
        r_len=len(matrix)
        c_len=len(matrix[0])
        for row in range(r_len):
            for col in range(c_len):
                if matrix[row][col]==0:
                    zeroes.append([row,col])
 
        for r,c in zeroes:
            for j in range(c_len):
                matrix[r][j]=0
            for i in range(r_len):
                matrix[i][c] = 0
            


        