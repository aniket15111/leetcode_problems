class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeros=0
        ones=0
        twoes=0

        for i in nums:
            if i==0:
                zeros+=1
            elif i==1:
                ones+=1
            else:
                twoes+=1
        for i in range(0,zeros):
            nums[i]=0
        for i in range(zeros,(ones+zeros)):
            nums[i]=1
        
        for i in range((ones+zeros),(ones+zeros+twoes)):
            nums[i]=2        
