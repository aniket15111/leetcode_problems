class Solution:
    def minPartitions(self, n: str) -> int:
        maximum=0
        for i in n:
            if(maximum<int(i)):
                maximum=int(i)
        return maximum
