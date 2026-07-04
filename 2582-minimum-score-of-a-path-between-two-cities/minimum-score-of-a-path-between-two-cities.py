import heapq as hq
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, dist in roads:
            adj[u].append((v, dist))
            adj[v].append((u, dist))
        

        ans=float('inf')
        q=deque([1])
        visited={1}
        while q:
            node=q.popleft()
            
            for i,dist in adj[node]:
                ans=min(ans,dist)
                if i not in visited:
                    visited.add(i)
                    q.append(i)
        return ans
