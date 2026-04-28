class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_ans=(n+1)//2
        odd_ans=n//2
        MOD = 10**9 + 7
        ans=self.power(5,even_ans,MOD)*pow(4,odd_ans,MOD)
        return ans%MOD

    def power(self,x,n,mod):
        if n==0:
            return 1
        ans=1
        x%=mod
        while n>0:
            if n%2==1:
                ans=(ans*x)%mod

            x=(x*x)%mod
            n=n//2
        return ans
    