# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        midi=None
        pos=-1
        for ind,i in enumerate(inorder):
            if i==preorder[0]:
                midi=preorder[0]
                pos=ind
                break
        lh=self.buildTree(preorder[1:pos+1],inorder[0:pos])
        rh=self.buildTree(preorder[pos+1:],inorder[pos+1:])
        root=TreeNode(midi)
        root.left=lh
        root.right=rh

        return root