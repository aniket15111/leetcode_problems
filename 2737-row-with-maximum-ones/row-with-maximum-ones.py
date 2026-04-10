class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_sum=0
        ans=[0,0]
        count=0
        for i in mat:
            if sum(i)>max_sum:
                max_sum=sum(i)
                ans=[count,max_sum]
            count+=1
        return ans