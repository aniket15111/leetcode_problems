import heapq as hq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        adj=defaultdict(list)

        for u,v,w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))

        dist=[float('inf')]*n
        ways=[0]*n

        dist[0]=0
        ways[0]=1

        pq=[(0,0)]

        while pq:
            d,u=hq.heappop(pq)
            if d>dist[u]:
                continue
            for v , time in adj[u]:
                if d+time<dist[v]:
                    dist[v]=d+time
                    ways[v]=ways[u]
                    hq.heappush(pq,(dist[v],v))
                elif d+time==dist[v]:
                    ways[v]=(ways[v]+ways[u])%(10**9 + 7)
        return ways[n-1]