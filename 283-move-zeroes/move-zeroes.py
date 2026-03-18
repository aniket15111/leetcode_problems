class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=0        
        for i in range(len(nums)):
            if nums[j]!=0 and nums[i]==0:
                j=i
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        
            
        