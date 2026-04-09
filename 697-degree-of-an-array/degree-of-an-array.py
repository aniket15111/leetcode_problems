class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first_idx = {}
        last_idx = {}
        counts = {}
        
        for i in range(len(nums)):
            num = nums[i]
            if num not in first_idx:
                first_idx[num] = i
            last_idx[num] = i            
            if num in counts:
                counts[num] = counts[num] + 1
            else:
                counts[num] = 1

        degree = max(counts.values())
        
        min_len = len(nums)
        
        for num in counts:
            if counts[num] == degree:
                length = last_idx[num] - first_idx[num] + 1
                if length < min_len:
                    min_len = length
                    
        return min_len