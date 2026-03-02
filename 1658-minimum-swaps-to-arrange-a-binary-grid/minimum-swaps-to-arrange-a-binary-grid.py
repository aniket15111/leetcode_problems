class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        end_zeros = []
        length = len(grid)
        swaps = 0

        # calculate trailing zeros
        for i in range(length):
            count = 0
            for j in range(length-1, -1, -1):
                if grid[i][j] == 1:
                    break
                count += 1
            end_zeros.append(count)

        for i in range(length):
            required = length - i - 1

            # If already valid, continue
            if end_zeros[i] >= required:
                continue

            # Find row to bubble up
            j = i + 1
            while j < length and end_zeros[j] < required:
                j += 1

            if j == length:
                return -1

            # Bubble upward
            while j > i:
                end_zeros[j], end_zeros[j-1] = end_zeros[j-1], end_zeros[j]
                swaps += 1
                j -= 1

        return swaps