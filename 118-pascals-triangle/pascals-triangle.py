class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for i in range(numRows):
            row = [1]
            prev = 1

            for j in range(1, i + 1):
                curr = prev * (i - j + 1) // j
                row.append(curr)
                prev = curr

            ans.append(row)

        return ans