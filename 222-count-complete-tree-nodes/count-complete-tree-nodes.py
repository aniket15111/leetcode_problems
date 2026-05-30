# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        cntleft=0
        temp1=root
        while temp1:
            cntleft+=1
            temp1=temp1.left
        cntright=0
        temp2=root
        while temp2:
            cntright+=1
            temp2=temp2.right

        if cntleft==cntright:
            return (2**cntleft)-1

        def get_tree_size(root):
            if root is None:
                return 0
        
            return 1 + get_tree_size(root.left) + get_tree_size(root.right)





        return 1+ get_tree_size(root.left)+get_tree_size(root.right)

