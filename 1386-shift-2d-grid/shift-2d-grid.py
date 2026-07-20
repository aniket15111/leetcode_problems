class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n=len(grid)
        m=len(grid[0])
        k=k%(n*m)
        for _ in range(k):
            ans=[[0 for _ in range(m)]for _ in range(n)]

            for i in range(n):
                for j in range(m):
                    if i==n-1 and j==m-1:
                        ans[0][0]=grid[i][j]
                    elif j==m-1 and i!=n-1:
                        ans[i+1][0]=grid[i][j]
                    else:
                        ans[i][j+1]=grid[i][j]
            grid=ans
        return grid
