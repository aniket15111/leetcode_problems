class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        #creating adj list because it is given in matrix
        adj={}
        n = len(prerequisites)

        for i in range(numCourses):
            adj[i]=[]

        for course, prereq in prerequisites:
                adj[prereq].append(course)
        
        visited=[0]*numCourses
        path_visited=[0]*numCourses
        result=[]
        def dfs(curr):
            if path_visited[curr]:
                return True
            if visited[curr]:
                return False

            visited[curr]=True
            path_visited[curr]=True

            for i in adj[curr]:
                if dfs(i):
                    return True

            result.append(curr)
            path_visited[curr]=False
            return False

        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return []
        return result[::-1]

            
        