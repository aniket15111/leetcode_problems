class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        
        length = 2**n - 1
        mid = length // 2 + 1
        
        if k < mid:
            return self.findKthBit(n-1, k)
        
        elif k == mid:
            return "1"
        
        else:
            ch = self.findKthBit(n-1, length - k + 1)
            return "1" if ch == "0" else "0"