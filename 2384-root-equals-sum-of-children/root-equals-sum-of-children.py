# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q=deque()
        q.append(root)
        while q: 
            temp=q.popleft()   

            if temp.left or temp.right:
                left_val=temp.left.val
                right_val=temp.right.val

                if left_val+right_val!=temp.val:
                    return False

            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            
        return True