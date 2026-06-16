class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:


        visited=[0]*len(graph)
        path_visited=[0]*len(graph)
        ans=[]
        def dfs(curr):
            if path_visited[curr]:
                return True
            if visited[curr]:
                return False

            visited[curr]=1
            path_visited[curr]=1

            for i in graph[curr]:
                if dfs(i):
                    return True
            path_visited[curr]=0
            return False


        
        for i in range(len(graph)):
            if not dfs(i):
                ans.append(i)
        return ans