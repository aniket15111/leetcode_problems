class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        q = deque([(0, 0, 1)])
    
        visited=set()
        visited.add((0,0))
        directions = [
                    (-1, -1), (-1, 0), (-1, 1),
                    (0, -1),           (0, 1),
                    (1, -1),  (1, 0),  (1, 1)
                ]
        while q:
            r,c,length=q.popleft()

            if r==n-1 and c==n-1:
                return length

            for dr,dc in directions:
                row=r+dr
                col=c+dc

                if row<0 or col<0 or row>n-1 or col>n-1 or grid[row][col]!=0 or (row,col)  in visited:
                    continue
                visited.add((row,col))
                q.append([row,col,length+1])

        return -1