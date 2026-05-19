'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
    
class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.data]
        res=[root.data]

        def addleft(node,res):
            temp=node.left
            while temp:
                if not temp.left and not temp.right:
                    break
                res.append(temp.data)
                if temp.left:
                    temp=temp.left
                else:
                    temp=temp.right
        def addroot(node,res):
            if not node.left and not node.right:
                res.append(node.data)
                return 
            if node.left:
                addroot(node.left,res)
            if node.right:
                addroot(node.right,res)
                
        def addright(node,res):
            temp=node.right
            right_res=[]
            while temp:
                if not temp.left and not temp.right:
                    break
                right_res.append(temp.data)
                if temp.right:
                    temp=temp.right
                else:
                    temp=temp.left
                
            
            res.extend(reversed(right_res))
            
        
        addleft(root,res)
        addroot(root,res)
        addright(root,res)
        
        return res
            
            
            
            
            