import heapq as hq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pq=[(0,0,0)]
        n=len(heights)
        m=len(heights[0])

        distance=[[float('inf') for _ in range(m)] for _ in range(n)]
        distance[0][0]=0
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        while pq:
            hgt,row,col=hq.heappop(pq)
            if row == n - 1 and col == m - 1:
                return hgt
            if hgt>distance[row][col]:
                continue
            for i,j in directions:
                new_row=row+i
                new_col=col+j

                if 0<=new_row<n and 0<=new_col<m:
                    new_effort=max(hgt,abs(heights[row][col]-heights[new_row][new_col]))

                    if new_effort<distance[new_row][new_col]:
                        distance[new_row][new_col]=new_effort
                        hq.heappush(pq,(new_effort,new_row,new_col))
        return 0
            
