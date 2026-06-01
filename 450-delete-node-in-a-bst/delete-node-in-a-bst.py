# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        dummy = TreeNode(0)
        dummy.left = root
        
        parent = dummy
        curr = root
        
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
                
        if not curr:
            return dummy.left
            
        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child
                
        else:
            succ_parent = curr
            successor = curr.right
            while successor.left:
                succ_parent = successor
                successor = successor.left
                
            curr.val = successor.val
            if succ_parent.left == successor:
                succ_parent.left = successor.right
            else:
                succ_parent.right = successor.right

        return dummy.left