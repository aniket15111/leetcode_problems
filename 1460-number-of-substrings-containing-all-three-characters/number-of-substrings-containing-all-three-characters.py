class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a={'a':0,'b':0,'c':0}
        n=len(s)
        if n<3:
            return 0
        i=0
        j=1

        ans=0
        a[s[0]]+=1

        while i<n:
            if a['a']>0 and a['b']>0 and a['c']>0:
                ans+=n-(j-1)
                a[s[i]]-=1
                i+=1
            elif j<n:
                a[s[j]]+=1
                j+=1
            else:
                break
        return ans
            
            

