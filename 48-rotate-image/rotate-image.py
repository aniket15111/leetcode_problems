class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        ans = [[0 for _ in range(n)] for _ in range(n)]

        for row in range(n):
            for col in range(n):
                ans[col][n - 1 - row] = matrix[row][col]

        # copy back into original matrix
        for i in range(n):
            for j in range(n):
                matrix[i][j] = ans[i][j]