class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        actual_sum = 0
        actual_sq_sum = 0
        
        for val in nums:
            actual_sum += val
            actual_sq_sum += val * val
            
        # 1. Expected sums for range [1, n]
        exp_sum = (n * (n + 1)) // 2
        exp_sq_sum = (n * (n + 1) * (2 * n + 1)) // 6
        
        # 2. Differences
        # diff_sum = x - y
        # diff_sq_sum = x^2 - y^2
        diff_sum = actual_sum - exp_sum
        diff_sq_sum = actual_sq_sum - exp_sq_sum
        
        # 3. Derive x + y
        # (x^2 - y^2) / (x - y) = (x + y)
        sum_xy = diff_sq_sum // diff_sum
        
        # 4. Solve for x (repeat) and y (missing)
        x = (diff_sum + sum_xy) // 2
        y = (sum_xy - diff_sum) // 2
        
        return [x, y]