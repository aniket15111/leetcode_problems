class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        ans=[]

        for i in s:
            if i=='(' or i=='[' or i=='{':
                ans.append(i)
            else:
                if len(ans)==0:
                    return False
                elif ans[-1]==mapping[i]:
                    ans.pop()
                else:
                    return False
        if len(ans)>0:
            return False
        return True
                