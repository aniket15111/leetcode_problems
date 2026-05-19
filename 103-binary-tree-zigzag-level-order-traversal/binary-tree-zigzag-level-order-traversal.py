# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q=[]
        res=[]
        q.append(root)
        levl=0

        while q:

            lenq=len(q)

            res.append([])

            for _ in range(lenq):
                node=q.pop(0)
                res[levl].append(node.val)
                if node.left is not None: q.append(node.left)
                if node.right is not None: q.append(node.right)
            if levl%2==1:
                res[levl].reverse()
            levl+=1
        return res