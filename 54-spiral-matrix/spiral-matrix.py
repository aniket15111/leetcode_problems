class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        srow, scol = 0, 0
        erow, ecol = n - 1, m - 1

        ans = []

        while srow <= erow and scol <= ecol:

            # top row
            for j in range(scol, ecol + 1):
                ans.append(matrix[srow][j])
            srow += 1

            # right column
            for i in range(srow, erow + 1):
                ans.append(matrix[i][ecol])
            ecol -= 1

            if srow <= erow:
                for j in range(ecol, scol - 1, -1):
                    ans.append(matrix[erow][j])
                erow -= 1

            if scol <= ecol:
                for i in range(erow, srow - 1, -1):
                    ans.append(matrix[i][scol])
                scol += 1

        return ans