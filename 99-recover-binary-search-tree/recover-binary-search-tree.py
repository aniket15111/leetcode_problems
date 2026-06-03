# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first=None
        self.second=None
        self.prev=None
        def dfs(node):
            if not node:
                return
            dfs(node.left)

            if self.prev and self.prev.val>node.val:
                if not self.first:
                    self.first=self.prev
                self.second=node

            self.prev=node

            dfs(node.right)

        dfs(root)

        if self.first and self.second:
            self.first.val,self.second.val=self.second.val,self.first.val