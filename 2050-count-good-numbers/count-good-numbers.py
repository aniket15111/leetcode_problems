class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_ans=(n+1)//2
        odd_ans=n//2
        MOD = 10**9 + 7
        ans=pow(5,even_ans,MOD)*pow(4,odd_ans,MOD)
        return ans%MOD
