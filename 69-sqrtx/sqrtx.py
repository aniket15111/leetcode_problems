class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        i, j = 2, x // 2
        
        while i <= j:
            pivot = i + (j - i) // 2
            num = pivot * pivot
            if num > x:
                j = pivot - 1
            elif num < x:
                i = pivot + 1
            else:
                return pivot
                
        return j