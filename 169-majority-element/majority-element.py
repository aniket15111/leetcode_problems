class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        element=0

        for i in nums:
            if cnt==0:
                element = i
                cnt+=1
            elif i==element:
                cnt+=1
            else:
                cnt-=1
        return element
    