class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)
        ans = [1] * n

        for i in range(1, n):
            ans[i] = ans[i-1] * arr[i-1]

        suffix = 1
        for i in range(n-1, -1, -1):
            ans[i] *= suffix
            suffix *= arr[i]

        return ans