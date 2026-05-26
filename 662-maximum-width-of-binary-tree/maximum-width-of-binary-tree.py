# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        q=deque()
        q.append([root,0])
        ans=0
        while q:
            size=len(q)
            mmin=q[0][1]

            first=None
            last=None

            for i in range(size):
                curr_id=q[0][1]-mmin
                node=q.popleft()[0]
                if i==0:
                    first=curr_id
                if i==size-1:
                    last=curr_id

                if node.left:
                    q.append([node.left,(curr_id*2)+1])
                if node.right:
                    q.append([node.right,(curr_id*2)+2])

            ans=max(last-first+1,ans)
        return ans