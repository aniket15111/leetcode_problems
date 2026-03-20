class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                
                for j in range(n-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        break
                
                nums[i:] = reversed(nums[i:])
                return
        
        nums.reverse()