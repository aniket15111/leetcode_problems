# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum=-float('inf')

        def check(node):
            if not node:
                return 0
            nonlocal maxsum
            
            lh=max(check(node.left),0)
            rh=max(check(node.right),0)
            currmax=node.val+lh+rh
            maxsum=max(maxsum,currmax)
            return node.val+max(lh,rh)

        check(root)
        return maxsum