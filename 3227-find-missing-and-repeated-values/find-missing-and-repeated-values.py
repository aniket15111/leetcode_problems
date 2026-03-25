class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = n * n
        
        actual_sum = 0
        actual_sq_sum = 0
        
        for row in grid:
            for val in row:
                actual_sum += val
                actual_sq_sum += val * val
                
        # 1. Calculate Expected Sums
        exp_sum = (m * (m + 1)) // 2
        exp_sq_sum = (m * (m + 1) * (2 * m + 1)) // 6
        
        # 2. Set up the equations
        # eq1: x - y = actual_sum - exp_sum
        # eq2: x^2 - y^2 = actual_sq_sum - exp_sq_sum
        diff_sum = actual_sum - exp_sum  # This is (x - y)
        diff_sq_sum = actual_sq_sum - exp_sq_sum  # This is (x^2 - y^2)
        
        # 3. Derive x + y
        # Since (x^2 - y^2) = (x - y)(x + y)
        # sum_xy = (x + y) = diff_sq_sum // diff_sum
        sum_xy = diff_sq_sum // diff_sum
        
        # 4. Solve for x and y
        # x = ((x - y) + (x + y)) // 2
        # y = ((x + y) - (x - y)) // 2
        x = (diff_sum + sum_xy) // 2
        y = (sum_xy - diff_sum) // 2
        
        return [x, y]