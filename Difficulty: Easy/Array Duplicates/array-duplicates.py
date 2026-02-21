class Solution:
    def findDuplicates(self, arr):
        a=set()
        ans=set()
        for i in arr:
            if i in a and i not in ans:
                ans.add(i)
            a.add(i)
        return list(ans)
        