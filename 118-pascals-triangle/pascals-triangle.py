class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
            ans=[]
            one=[1]
            row=[]
            for i in range(numRows+1):
                row=[]
                row.append(1)
                count=0
                rev=i-1
                for j in range(1,i):
                    element=row[count]*rev//j
                    rev-=1
                    count+=1
                    row.append(element)
                ans.append(row)
            return ans[1:]
