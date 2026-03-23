class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        prev = 1

        for j in range(1, rowIndex + 1):
            curr = prev * (rowIndex - j + 1) // j
            row.append(curr)
            prev = curr
        return row