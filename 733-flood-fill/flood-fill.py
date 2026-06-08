class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows,cols=len(image),len(image[0])
        visited=set()
        start_color=image[sr][sc]
        if start_color == color:
            return image
        def dfs(r,c):
            if (r<0 or r>=rows or c<0 or c>=cols or (r,c) in visited or image[r][c]!=start_color):
                return 
            
            visited.add((r,c))

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            image[r][c]=color
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        dfs(sr,sc)
        return image