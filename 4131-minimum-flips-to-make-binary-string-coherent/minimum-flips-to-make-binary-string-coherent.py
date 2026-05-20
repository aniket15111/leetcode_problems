class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        total_ones = s.count('1')
        total_zeros = n - total_ones
        res = total_ones
  
        res = min(res, total_zeros)

        
        if total_ones > 0:
            res = min(res, total_ones - 1)
        else:
            res = min(res, 1) 
            
        if n >= 2:
            mid_ones = total_ones - (1 if s[0] == '1' else 0) - (1 if s[-1] == '1' else 0)
            end_flips = (1 if s[0] == '0' else 0) + (1 if s[-1] == '0' else 0) + mid_ones
            res = min(res, end_flips)
        
        return res