class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance_mat = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            distance_mat[i][i] = 0
        for u, v, w in edges:
            distance_mat[u][v] = w
            distance_mat[v][u] = w
            
        # Floyd-Warshall Algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distance_mat[i][j] > distance_mat[i][k] + distance_mat[k][j]:
                        distance_mat[i][j] = distance_mat[i][k] + distance_mat[k][j]
                        
        min_reached_cnt = float('inf')
        ans = -1

        for i in range(n):
            reachable_cities = 0 
            for j in range(n):
                if i != j and distance_mat[i][j] <= distanceThreshold:
                    reachable_cities += 1
                    

            if reachable_cities <= min_reached_cnt: 
                min_reached_cnt = reachable_cities 
                ans = i         
                
        return ans