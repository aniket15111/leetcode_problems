# Node class
''' class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None 
'''

# Stack class template
class myStack:

    def __init__(self):
        self.top=None
        self._size=0

    def isEmpty(self):
        if self.top:
            return False
        return True
        

    def push(self, x):
        head=Node(x)
        head.next=self.top
        self.top=head
        self._size+=1

    def pop(self):
        # Removes an element from the top of the stack
        if self.isEmpty():
            return -1
        self.top=self.top.next
        self._size-=1
        

    def peek(self):
        # Returns the top element of the stack
        # If the stack is empty, return -1
        if self.isEmpty():
            return -1
        return self.top.data


    def size(self):
        # Returns the current size of the stack
        
        return self._size