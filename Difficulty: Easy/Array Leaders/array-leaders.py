
class Solution:
    def leaders(self, arr):
        ans = []
        n = len(arr)
        
        max_from_right = arr[-1]
        ans.append(max_from_right)
        
        for i in range(n-2, -1, -1):  # start from second last
            if arr[i] >= max_from_right:
                ans.append(arr[i])
                max_from_right = arr[i]
        
        ans.reverse()
        return ans