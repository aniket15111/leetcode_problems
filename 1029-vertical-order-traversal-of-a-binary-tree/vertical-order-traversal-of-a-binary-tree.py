# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, node: Optional[TreeNode]) -> List[List[int]]:
      
        cnt=0
        if not node:
            return []
        
        queue = deque([(node, 0,0)])
        c_table=defaultdict(list)
        
        while queue:
            temp,row,col = queue.popleft()
            c_table[col].append((row,temp.val))
            
            if temp.left:
                queue.append((temp.left,row+1,col-1))
            if temp.right:
                queue.append((temp.right,row+1,col+1))
        ans=[]
        for col in sorted(c_table.keys()):
            c_table[col].sort()
            ans.append([val for row,val in c_table[col]])
        return ans


            

            
            