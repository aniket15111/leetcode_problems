class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prev=0
        ans=0
        for i in gain:
            prev+=i
            ans=max(ans,prev)

        return ans