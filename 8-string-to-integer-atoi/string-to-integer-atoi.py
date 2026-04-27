class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if not s:
            return 0
        negative=1
        Mini= -2147483648
        Maxi= 2147483647
        if s[0]=='-':
            negative=-1
            s=s[1:]
        elif s[0]=='+':
            s=s[1:]
        ans=0
        for i in s:
            if i <'0' or i>'9':
                break
            ans=(ans*10)+ int(i)
        ans*=negative
        if ans < Mini:
            return Mini
        if ans > Maxi:
            return Maxi
            
        return ans