class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n=len(mat)
        m=len(mat[0])
        visited=[[False for _ in range(m)] for _ in range(n)]
        distance=[[0 for _ in range(m)] for _ in range(n)]
        q=deque()

        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    q.append((i,j,0))
                    visited[i][j]=True
    
        direction=((1,0),(-1,0),(0,1),(0,-1))
        while q:
            row,col,dist=q.popleft()
            for i,j in direction:
                new_row = row + i
                new_col = col + j
                if new_row<0 or new_row>=n or new_col<0 or new_col>=m or visited[new_row][new_col]==True:
                    continue
                
                visited[new_row][new_col]=True
                q.append((new_row,new_col,dist+1))
                distance[new_row][new_col]=dist+1
        return distance