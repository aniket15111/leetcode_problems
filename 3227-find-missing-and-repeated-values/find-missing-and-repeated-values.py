class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = n * n
        num = set()
        repeat = 0
        actual_sum = 0
        
        for row in grid:
            for val in row:
                actual_sum += val
                if val in num:
                    repeat = val
                else:
                    num.add(val)
        
        expected_sum = (m * (m + 1)) // 2
        missing = repeat + expected_sum - actual_sum
        
        return [repeat, missing]