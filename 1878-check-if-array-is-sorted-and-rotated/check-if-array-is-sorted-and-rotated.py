class Solution:
    def check(self, nums: List[int]) -> bool:
        counter=0
        n=len(nums)
        for i in range(1,n):
            
            if(nums[i-1]>nums[i]):
                counter+=1
                if(nums[0]<nums[n-1]):
                    return False
            if counter==2:
                return False
        return True
                