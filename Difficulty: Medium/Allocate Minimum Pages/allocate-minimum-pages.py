class Solution:
    def findPages(self, arr, k):
        if k > len(arr):
            return -1
            
        i = max(arr)
        j = sum(arr)
        ans = j
        
        while i <= j:
            mid = (i + j) // 2
            
            if self.fun(arr, k, mid):
                ans = mid
                j = mid - 1
            else:
                i = mid + 1
        return ans
            
    def fun(self, arr, k, mid):
        current_sum = 0
        count = 1
        
        for pages in arr:
            if (pages + current_sum) > mid:
                count += 1
                current_sum = pages
                if count > k:
                    return False
            else:
                current_sum += pages
        return True