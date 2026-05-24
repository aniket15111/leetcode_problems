# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]

        def pathhelp(node,current_path):
            if not node:
                return 
            if current_path:
                current_path+='->'+ str(node.val)
            else:
                current_path=str(node.val)
            
            if not node.left and not node.right:
                ans.append(current_path)

            else:
                pathhelp(node.left,current_path)
                pathhelp(node.right,current_path)
            
        pathhelp(root, '')
        return ans     


        pathhelp(root,'')
        return ans

            