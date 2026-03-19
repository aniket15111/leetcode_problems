class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        positive=[]
        negative=[]
        
        for i in nums:
            if i<0:
                positive.append(i)
            else:
                negative.append(i)
        positive_counter=0
        negative_counter=0
        for i in range(0,n):
            if i%2!=0:
                nums[i]=positive[positive_counter]
                positive_counter+=1
            else:
                nums[i]=negative[negative_counter]
                negative_counter+=1
        return nums