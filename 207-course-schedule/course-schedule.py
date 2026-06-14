from collections import deque
from typing import List

class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
            
        
        adj = {i: [] for i in range(n)}
        indegree = [0] * n
        
        for row in prerequisites:
            u, v = row[0], row[1]  
            adj[v].append(u)
            indegree[u] += 1
            
        q = deque()
        
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                
        count = 0
        
        while q:
            curr = q.popleft()
            count += 1
            
            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
                    
        return count == n