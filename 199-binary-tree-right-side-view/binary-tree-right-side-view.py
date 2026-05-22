# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue=deque([(root,0)])
        dt={}

        while queue:
            node,row=queue.popleft()

            dt[row]=node.val

            if node.left:
                queue.append((node.left,row+1))
            if node.right:
                queue.append((node.right,row+1))

        return [dt[i] for i in range(len(dt))]