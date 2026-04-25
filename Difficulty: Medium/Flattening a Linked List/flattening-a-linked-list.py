'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''




class Solution:
    def merge(self, a, b):
        dummy = Node(-1)
        temp = dummy
        
        while a and b:
            if a.data < b.data:
                temp.bottom = a
                a = a.bottom
            else:
                temp.bottom = b
                b = b.bottom
            temp = temp.bottom
            
        if a:
            temp.bottom = a
        else:
            temp.bottom = b
            
        if dummy.bottom:
            dummy.bottom.next = None
        
        return dummy.bottom
    
    def flatten(self, root):
        if root == None or root.next == None:
            return root
        
        root.next = self.flatten(root.next)
        
        root = self.merge(root, root.next)
        
        return root