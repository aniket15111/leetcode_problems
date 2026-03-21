class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for row in range(n):
            for col in range(n):
                if(row < col):
                    continue
                matrix[row][col],matrix[col][row]=matrix[col][row],matrix[row][col]

        for row in matrix:
            row.reverse()
            
