class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        qu=deque()
        ans=[]
        for i in range(len(nums)):
            while qu and nums[qu[-1]]<nums[i]:
                qu.pop()      
            qu.append(i)

            if qu[0]==i-k:
                qu.popleft()

            
            if i>=k-1:
                ans.append(nums[qu[0]])

        
        return ans

                