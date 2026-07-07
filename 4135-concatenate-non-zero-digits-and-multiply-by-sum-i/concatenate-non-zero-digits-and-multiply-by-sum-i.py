class Solution:
    def sumAndMultiply(self, n: int) -> int:
        strn=str(n)
        ans=0
        sumi=0
        for i in strn:
            inti=int(i)
            if inti !=0:
                ans=(ans*10)+inti
                sumi+=inti
        return ans*sumi


