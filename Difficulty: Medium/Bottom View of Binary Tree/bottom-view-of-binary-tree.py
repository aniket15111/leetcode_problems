'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        if not root:
            return 
        queue=deque([(root,0)])
        dt={}
        
        while queue:
            node,col=queue.popleft()
            
            dt[col]=node.data
                
            if node.left:
                queue.append((node.left,col-1))
            if node.right:
                queue.append((node.right,col+1))
        return [dt[hd] for hd in sorted(dt.keys())]
        
        