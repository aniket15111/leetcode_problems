class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check={}
        if len(s) != len(t):
            return False

        for i in s:
            if(i not in check):
               check[i]=1
            else:
                check[i]+=1
        for i in t:
            if(i not in check):
                return False
            else:
                check[i]-=1
                if(check[i]==-1):
                  return False
        return True