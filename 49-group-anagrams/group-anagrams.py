class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for i in strs:
            a=''.join(sorted(i))
            if(a not in ans):
                ans[a]=[]
            ans[a].append(i)
        return list(ans.values())