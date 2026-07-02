class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        health_lost = [[float('inf')] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q=deque([(0,0)])
        health_lost[0][0] =grid[0][0]
        while q:
            r, c = q.popleft()
            if r==m-1 and c==n-1:
                break

            for dr, dc in directions:
                nr,nc=r+dr, c+dc

                if 0<=nr<m and 0<=nc<n:
                    loss=health_lost[r][c]+grid[nr][nc]

                    if loss<health_lost[nr][nc]:
                        health_lost[nr][nc]=loss

                        if grid[nr][nc]==0:
                            q.appendleft((nr,nc))

                        else:
                            q.append((nr,nc))
        return health-health_lost[m-1][n-1]>=1
