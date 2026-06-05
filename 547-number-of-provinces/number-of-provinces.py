class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V=len(isConnected)
        visited=[False]*V
        q=deque()
        cnt=1
        q.append(0)
        visited[0]=True
        next_start=1

        while q :
            curr=q.popleft()
            if  visited[curr]==False:
                cnt+=1
            
            for i in range(V):
                if isConnected[curr][i]==1 and  not visited[i]:
                    visited[i]=True
                    q.append(i)
            if  not q:
                for i in range(next_start,V):
                    if visited[i]==False:
                        visited[i]=True
                        cnt+=1
                        q.append(i)
                        next_start=i+1
                        break
        return cnt