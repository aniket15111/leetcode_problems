import heapq as hq
from collections import defaultdict
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        adj=defaultdict(list)
        
        for i,j,k in edges:
            adj[i].append([k,j])
            adj[j].append([k,i])
        
        pq=[]
        dist=[float('inf')]*V
        dist[src]=0
        hq.heappush(pq,[0,src])
        
        while pq:
            curr, node = hq.heappop(pq)
            if curr>dist[node]:
                continue
            for l,m in adj[node]:
                if curr+l<dist[m]:
                    dist[m]=curr+l
                    hq.heappush(pq,[dist[m],m])
        return dist
                
            