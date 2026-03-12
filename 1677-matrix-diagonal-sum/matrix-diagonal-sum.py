class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagonal_sum = 0
        counter = len(mat[0]) - 1
        n = len(mat)

        for i in range(len(mat)):
            if n % 2 != 0 and i == (n-1)//2 and counter == (n-1)//2:
                diagonal_sum += mat[i][i]
                counter -= 1
                continue

            diagonal_sum += mat[i][i] + mat[i][counter]
            counter -= 1

        return diagonal_sum