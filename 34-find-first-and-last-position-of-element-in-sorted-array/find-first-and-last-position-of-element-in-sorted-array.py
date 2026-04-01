class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_lower(n, t):
            i, j = 0, len(n) - 1
            ans = -1
            while i <= j:
                mid = (i + j) // 2
                if n[mid] < t:
                    i = mid + 1
                else:
                    if n[mid] == t: 
                        ans = mid
                    j = mid - 1 
            return ans

        def find_upper(n, t):
            i, j = 0, len(n) - 1
            ans = -1
            while i <= j:
                mid = (i + j) // 2
                if n[mid] <= t:
                    if n[mid] == t: 
                        ans = mid
                    i = mid + 1
                else:
                    j = mid - 1
            return ans

        return [find_lower(nums, target), find_upper(nums, target)]