# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        st1=[root]
        st2=[]
    
        while st1:
            curr=st1.pop()
            st2.append(curr.val)
            if curr.left:
                st1.append(curr.left)
            if curr.right:
                st1.append(curr.right)
            

        st2.reverse()

        return st2