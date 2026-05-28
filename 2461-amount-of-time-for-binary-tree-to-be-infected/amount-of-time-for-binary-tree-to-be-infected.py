from collections import deque

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0

        q = deque([root])
        backward = {}
        start_node = None

        while q:
            temp = q.popleft()
            if temp.val == start:
                start_node = temp
                
            if temp.left:
                q.append(temp.left)
                backward[temp.left] = temp
            if temp.right: 
                q.append(temp.right)
                backward[temp.right] = temp
        
        q = deque([start_node])
        visited = {start_node}
        minutes = -1 
        while q:
            minutes += 1
            for _ in range(len(q)):
                curr = q.popleft()
                
                if curr.left and curr.left not in visited:
                    visited.add(curr.left)
                    q.append(curr.left)
                    
                if curr.right and curr.right not in visited:
                    visited.add(curr.right)
                    q.append(curr.right)
                    
                if curr in backward and backward[curr] not in visited:
                    visited.add(backward[curr])
                    q.append(backward[curr])
                    
        return minutes