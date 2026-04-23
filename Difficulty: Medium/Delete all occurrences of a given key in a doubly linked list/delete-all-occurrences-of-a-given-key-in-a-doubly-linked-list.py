'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        curr=head
        
        while curr:
            if curr.data==x:
                next_node=curr.next
                
                if curr==head:
                    head=curr.next
                
                if curr.prev:
                    curr.prev.next=curr.next
                    
                if curr.next:
                    curr.next.prev=curr.prev
                
                curr=next_node
            else:
                curr=curr.next
        
        return head
            