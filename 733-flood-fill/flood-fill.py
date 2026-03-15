class Solution:
    def dfs(self, image, i, j, new_color, original_color):
        # 1. Check boundaries
        # 2. Check if the current pixel is actually the color we want to change
        if (i < 0 or i >= len(image) or 
            j < 0 or j >= len(image[0]) or 
            image[i][j] != original_color):
            return

        # Change the color of the current pixel
        image[i][j] = new_color

        # Recursively visit all 4 neighbors
        self.dfs(image, i + 1, j, new_color, original_color) # Down
        self.dfs(image, i - 1, j, new_color, original_color) # Up
        self.dfs(image, i, j + 1, new_color, original_color) # Right
        self.dfs(image, i, j - 1, new_color, original_color) # Left

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        
        # Optimization: If the target color is the same as the original, 
        # doing a DFS will cause an infinite loop or redundant work.
        if original_color == color:
            return image
        
        self.dfs(image, sr, sc, color, original_color)
        
        return image