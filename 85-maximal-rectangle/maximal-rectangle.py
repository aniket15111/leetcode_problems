class Solution:

    def mat(self,matrix):
        if not matrix or not matrix[0]:
            return[]
        n=len(matrix)
        m=len(matrix[0])
        pref = [[0 for _ in range(m)] for _ in range(n)]
        for j in range(m):
            sumi=0
            for i in range(n):
                if matrix[i][j]=='1' or matrix[i][j]==1:
                    sumi+=1
                else: 
                    sumi=0
                pref[i][j]=sumi
        return pref

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        pref=self.mat(matrix)
        ans=0

        if not matrix:
            return 0

        n=len(pref[0])
        for i in pref:
            st=[]
            for j in range(n+1):
                current_height= i[j] if j<n else 0 
                while st and i[st[-1]]>current_height:
                    h=i[st.pop()]

                    w= j if not st else j- st[-1]-1

                    ans=max(ans,h*w)
                st.append(j)
        return ans