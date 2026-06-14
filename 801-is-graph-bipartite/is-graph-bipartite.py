class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        n=len(graph)
        visited=[-1]*n

        for i in range(n):
            if visited[i]!=-1:
                continue
            q=deque([i])

            visited[i]=0

            while q:
                curr=q.popleft()

                for i in graph[curr]:
                    if visited[i]==-1:
                        visited[i]=1-visited[curr]
                        q.append(i)
                    elif visited[i]==visited[curr]:
                        return False
        return True