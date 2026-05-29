class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=float(inf)
        for i in nums:
            sumi=0
            digit=i
            while digit:
                sumi+=digit%10
                digit=digit//10
            ans=min(sumi,ans)

        return int(ans)