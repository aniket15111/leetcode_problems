from typing import List
from collections import defaultdict
import heapq as hq
class Solution:
    def shortestPath(self,n:int, q:int, edges:List[List[int]] )->List[int]:
        adj=defaultdict(list)
        for u,v,w in edges:
            adj[u].append((w,v))
            adj[v].append((w, u))
            
        dist=[float('inf')]*(n+1)
        parent = [i for i in range(n + 1)]
        
        pq=[]
        hq.heappush(pq,(0,1))
        dist[1]=0
        while pq:
            curr,node=hq.heappop(pq)
            
            if curr>dist[node]:
                continue
            for l,m in adj[node]:
                if curr+l<dist[m]:
                    parent[m]=node
                    dist[m]=curr+l
                    hq.heappush(pq,(dist[m],m))
                    
        if dist[n]==float('inf'):
            return [-1]
        
        path=[]
        current=n
        while parent[current]!=current:
            path.append(current)
            current=parent[current]
        path.append(1)
        path.reverse()
        return [dist[n]]+path
        

            
                    
                    
            
        
            