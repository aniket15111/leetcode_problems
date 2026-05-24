"""
Definition of Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""
from collections import deque
class Solution:
    def Paths(self, root):
        ans = []
        
        def dfs(node, current_path):
            if not node:
                return
            
            current_path.append(node.data)
            
            if not node.left and not node.right:
                ans.append(list(current_path))
            else:
                dfs(node.left, current_path)
                dfs(node.right, current_path)
            
            current_path.pop()

        dfs(root, [])
        return ans