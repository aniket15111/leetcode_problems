# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr=root
        res=[]
        while curr:
            if curr.left is None:
                res.append(curr.val)
                curr=curr.right

            else:
                link=curr.left
                while link.right and link.right!=curr:
                    link=link.right


                if link.right is None:
                    link.right=curr
                    curr=curr.left
                else:
                    link.right=None
                    res.append(curr.val)
                    curr=curr.right
        return res
                
                    
                