# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map={}


        for idx,i in enumerate(inorder):
            inorder_map[i]=idx

        counter=0

        def helper(left,right):
            nonlocal counter
            if left>right:
                return None

            val_root=preorder[counter]
            root=TreeNode(val_root)

            counter+=1

            pivot=inorder_map[val_root]

            root.left=helper(left,pivot-1)
            root.right=helper(pivot+1,right)

            return root

        return helper(0,len(inorder)-1)


