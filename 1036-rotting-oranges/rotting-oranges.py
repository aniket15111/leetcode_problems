class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        fresh=0
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        minut=0
        while q:
            n=len(q)
            rotten_any = False
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            for i in range(n):
                r,c=q.popleft()
                for dr,dc in directions:
                    next_r, next_c = r + dr, c + dc
                    if (0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == 1):
                        grid[next_r][next_c] = 2
                        q.append((next_r,next_c))
                        fresh-=1
                        rotten_any=True

            if rotten_any:
                minut+=1
        return minut if fresh == 0 else -1
            