class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        matrix = [[-1 for _ in range(len(s))] for _ in range(numRows)]
        kreach=False
        j=0
        k=0
        for i in s :
            matrix[j][k]=i
            if j==0 or j==numRows-1:
                kreach=not kreach
            if kreach:
                j+=1
            else:
                j-=1
                k+=1
        return "".join(num for row in matrix for num in row if num != -1)


