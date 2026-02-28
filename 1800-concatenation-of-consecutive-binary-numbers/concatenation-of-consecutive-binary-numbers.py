class Solution:
    def concatenatedBinary(self, n: int) -> int:
        num=0
        for i in range(1,n+1):
            digit=int( math.log2(i))+1
            num = ((num << digit) + i) % (10**9+7)
        return num
