class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=''
        count = 0

        for i in range(len(s)):
            if count==0:
                count+=1
            elif s[i]=='(':
                ans+=s[i]
                count+=1
            elif s[i]==')' and count==1:
                count-=1
            else:
                ans+=s[i]
                count-=1
        return ans
