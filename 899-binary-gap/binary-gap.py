class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        
        first_one = 0
        adj = 0
        max_adj = 0
        
        for i in binary:
            
            if i == '1':
                if first_one == 1:
                    if adj > max_adj:
                        max_adj = adj
                first_one = 1
                adj = 1  
            
            elif first_one == 1:
                adj += 1
        
        return max_adj