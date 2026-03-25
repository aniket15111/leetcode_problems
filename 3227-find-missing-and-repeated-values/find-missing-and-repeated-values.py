class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_elements = n * n
        num = set()
        repeat = 0
        expected_sum=0
        count=1
        actual_sum=0
        for i in range(n):
            for j in range(n):
                if grid[i][j] in num:
                    repeat = grid[i][j]
                else:
                    num.add(grid[i][j])
                expected_sum+=count
                actual_sum+=grid[i][j]
                count+=1
        

        missing = repeat-actual_sum+expected_sum
        
                
        return [repeat, missing]