class Solution:
    def dfs(self, adj):
        v=len(adj)
        visited=[False]*v
        res=[]

        def dfsrec(adj, visited, s, res):
            visited[s]=True
            res.append(s)
            
            for i in adj[s]:
                if not visited[i]:
                    dfsrec(adj, visited, i, res)
                    
        dfsrec(adj,visited,0,res)

        return res