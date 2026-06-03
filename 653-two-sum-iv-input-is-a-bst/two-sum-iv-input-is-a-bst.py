# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hm=set()

        def dfs(node):
            if node is None:
                return False
            
            if dfs(node.left): 
                return True
            if k-node.val in hm:
                return True
            hm.add(node.val)
            
            return dfs(node.right)

        return dfs(root)