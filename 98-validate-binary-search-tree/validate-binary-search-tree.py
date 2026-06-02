# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        prev=float('-inf')
        def dfs(node):
            nonlocal prev
            if node is None:
                return True
            if not dfs(node.left):
                return False
            if prev>=node.val:
                return False
            prev=node.val
            return dfs(node.right)

        return  dfs(root)