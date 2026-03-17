class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        new = nums + nums
        nums[:] = new[n - k : 2*n - k]