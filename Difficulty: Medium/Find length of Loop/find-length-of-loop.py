'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                break
                
        if slow!=fast or slow.next==None:
            return 0
        counter=1
        slow=slow.next
        
        while slow!=fast:
            slow=slow.next
            counter+=1
            
        return counter
            
        