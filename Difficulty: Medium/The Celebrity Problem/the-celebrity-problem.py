class Solution:
    def celebrity(self, mat):
        knowme=[0]*len(mat)
        iknow=[0]*len(mat)
        
        for i in range(len(mat)):
            for j in range(len(mat)):
                if mat[i][j]==1:
                    knowme[j]+=1
                    iknow[i]+=1
                    
                    
        for i in range(len(mat)):
            if knowme[i] == n and iknow[i]==1:
                return i
        return -1