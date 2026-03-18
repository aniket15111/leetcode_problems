class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=sum(nums)
        req=n*(n+1)//2
        return req-total