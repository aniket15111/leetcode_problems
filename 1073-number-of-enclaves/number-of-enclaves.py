class Solution:
    def numEnclaves(self, board: List[List[int]]) -> int:
        n=len(board)
        m=len(board[0])
        visited=[[False for _ in range(m)] for _ in range(n)]
        def dfs(row,col):
            if row<0 or row>=n or col<0 or col>=m:
                return
            if  board[row][col]==0 or visited[row][col]==True:
                return
            visited[row][col]=True
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)

        for i in range(n):
            if board[i][0]==1 and not visited[i][0]:
                dfs(i,0)
            if board[i][m-1]==1 and not visited[i][m-1]:
                dfs(i,m-1)

        for i in range(m):
            if board[0][i]==1 and not visited[0][i]:
                dfs(0,i)
            if board[n-1][i]==1 and not visited[n-1][i]:
                dfs(n-1,i)
        cnt=0
        for i in range(n):
            for j in range(m):
                if board[i][j]==1 and not visited[i][j]:
                    cnt+=1

        return cnt