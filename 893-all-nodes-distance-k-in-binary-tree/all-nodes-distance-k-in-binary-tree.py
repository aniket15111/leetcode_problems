# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        q = deque([root])
        backward = {}

        while q:
            temp = q.popleft() 
            if temp.left:
                q.append(temp.left)
                backward[temp.left] = temp
            if temp.right: 
                q.append(temp.right)
                backward[temp.right] = temp
        
        q.append((target, 0))  
        visited = {target}
        result = []

        while q: 
            node, dist = q.popleft()

            if dist == k:
                result.append(node.val)
            elif dist < k:
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    q.append((node.left, dist + 1))
                
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    q.append((node.right, dist + 1))
                
                if node in backward and backward[node] not in visited:
                    visited.add(backward[node])
                    q.append((backward[node], dist + 1))

        return result