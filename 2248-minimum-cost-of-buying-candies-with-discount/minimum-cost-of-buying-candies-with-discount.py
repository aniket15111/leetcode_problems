class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        i=0
        cnt=0
        ans=0
        while i<len(cost):
            if cnt==2:
                i+=1
                cnt=0
                continue
            else:
                cnt+=1
                ans+=cost[i]
                i+=1
        return ans


