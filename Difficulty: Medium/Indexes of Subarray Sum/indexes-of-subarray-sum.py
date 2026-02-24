class Solution:
    def subarraySum(self, arr, s):
        start = 0
        current_sum = 0
        
        for end in range(len(arr)):
            current_sum += arr[end]
            
            while current_sum > s and start <= end:
                current_sum -= arr[start]
                start += 1
            
            if current_sum == s:
                return [start + 1, end + 1]   # 1-based index
        
        return [-1]