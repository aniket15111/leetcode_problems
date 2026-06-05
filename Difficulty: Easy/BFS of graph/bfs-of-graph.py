class Solution:
    def bfs(self, adj):
        V=len(adj)
        
        visited=[False]*V
        res=[]
        q=deque()
        q.append(0)
        visited[0]=True
        
        
        while q:
            curr=q.popleft()
            res.append(curr)
            
            for i in adj[curr]:
                if visited[i]==False:
                    visited[i]=True
                    q.append(i)
                    
        return res