class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])

        visited=[[False for _ in range(m) ] for _ in range(n)]

        cnt=0
        directions=[(-1,0),(1,0),(0,-1),(0,1)]

        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and visited[i][j]==False:
                    visited[i][j]=True
                    cnt+=1
                    q=deque([(i,j)])
                    

                    while q:

                        row,col=q.popleft()

                        for k,l in directions:
                            new_row=row+k
                            new_col=col+l

                            if 0<=new_row<n and 0<=new_col<m and grid[new_row][new_col]=='1' and not visited[new_row][new_col]:
                                visited[new_row][new_col]=True
                                q.append((new_row,new_col))

        return cnt