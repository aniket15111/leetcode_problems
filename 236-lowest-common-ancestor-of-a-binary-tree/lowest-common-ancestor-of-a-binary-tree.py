# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        anslist1=[]
        anslist2=[]
        def dfs(node,an):
            nonlocal anslist1, anslist2
            if not node:
                return
            an.append(node)
            if node==p:
                anslist1=an.copy()
            if node==q:
                anslist2=an.copy()
            
            dfs(node.left,an)
            dfs(node.right,an)
            an.pop()

        dfs(root,[])
        lca_node = None
        for i in range(min(len(anslist1),len(anslist2))):
            if anslist1[i]!=anslist2[i]:
                break
            else:
                lca_node=anslist1[i]

        return lca_node
                