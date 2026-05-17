# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=0
        def findmax(node):
            nonlocal maxi
            if not node:
                return 0
            lh=findmax(node.left)
            rh=findmax(node.right)
            maxi=max(maxi,lh+rh)
            return 1+max(lh,rh)
        findmax(root)
        return maxi
