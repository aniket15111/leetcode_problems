class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s

        flips1 = 0
        flips2 = 0
        res = n
        left = 0

        for right in range(len(s)):
            if s[right] != ('0' if right % 2 == 0 else '1'):
                flips1 += 1
            if s[right] != ('1' if right % 2 == 0 else '0'):
                flips2 += 1

            if right-left+1>n:
                if s[left]!=('0' if left%2==0 else'1'):
                    flips1-=1
                if s[left]!=('1' if left %2==0 else '0'):
                    flips2-=1
                left+=1
            if right-left+1==n:
                res=min(res,flips1,flips2)
        return res