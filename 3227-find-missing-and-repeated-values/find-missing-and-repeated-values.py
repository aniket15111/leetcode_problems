class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_elements = n * n
        num = set()
        repeat = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] in num:
                    repeat = grid[i][j]
                else:
                    num.add(grid[i][j])
        

        missing = 0
        for i in range(1, total_elements + 1):
            if i not in num:
                missing = i
                break
                
        return [repeat, missing]