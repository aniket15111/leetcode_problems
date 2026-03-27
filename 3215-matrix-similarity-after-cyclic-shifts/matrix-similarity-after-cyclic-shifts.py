class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        cols = len(mat[0])
        shift = k % cols
        
        if shift == 0:
            return True
            
        for row in mat:
            for j in range(cols):
                if row[j] != row[(j + shift) % cols]:
                    return False
                    
        return True
