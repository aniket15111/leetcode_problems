# Node class
class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Queue class template
class myQueue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.leng = 0
        
    def isEmpty(self):
        # Always use self. to access instance variables
        return self.front is None

    def enqueue(self, x):
        temp = Node(x)
        # If the queue is empty, the new node is both front and rear
        if self.rear is None:
            self.front = self.rear = temp
        else:
            # Link the old rear to the new node, then move rear
            self.rear.next = temp
            self.rear = temp
        self.leng += 1

    def dequeue(self):
        if self.isEmpty():
            return -1
        
        # 1. Save the data to return it later
        popped_val = self.front.data
        
        # 2. Move the front pointer forward
        self.front = self.front.next
        
        # 3. CRITICAL: If front becomes None, the queue is now empty
        # So rear must also be None
        if self.front is None:
            self.rear = None
            
        self.leng -= 1
        return popped_val

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.front.data

    def size(self):
        return self.leng