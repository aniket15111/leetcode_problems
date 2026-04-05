class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        i = max(weights) 
        j = sum(weights)
        ans = j
        
        while i <= j:
            capacity = (i + j) // 2
            if self.fun(weights, capacity, days):
                ans = capacity
                j = capacity - 1
            else:
                i = capacity + 1
        return ans

    def fun(self, arr, mid, x):
        wsum = 0
        count = 1
        for val in arr:
            if wsum + val > mid:
                count += 1
                wsum = val
            else:
                wsum += val
        
        return count <= x