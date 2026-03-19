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
        for i in range(0,len(nums)):
            if(zeros>0):
                nums[i]=0
                zeros-=1
                continue
            if(ones>0):
                nums[i]=1
                ones-=1
                continue
            nums[i]=2
            