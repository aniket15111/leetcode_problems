# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map={}


        for idx,i in enumerate(inorder):
            inorder_map[i]=idx

        counter=len(inorder)-1

        def helper(left,right):
            nonlocal counter
            if left>right:
                return None

            root_val=postorder[counter]
            root=TreeNode(root_val)

            counter-=1

            pivot=inorder_map[root_val]

            root.right = helper(pivot + 1, right)
            root.left = helper(left, pivot - 1)

            return root
        return helper(0,len(inorder)-1)