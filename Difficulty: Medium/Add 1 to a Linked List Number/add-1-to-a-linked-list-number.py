'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self, head):

        prev = None
        current = head

        while current:
            front = current.next
            current.next = prev
            prev = current
            current = front

        head = prev

        carry = 1
        temp = head
        prev = None

        while temp and carry:
            total = temp.data + carry
            temp.data = total % 10
            carry = total // 10

            prev = temp
            temp = temp.next

        if carry:
            prev.next = Node(carry)

        prev = None
        current = head

        while current:
            front = current.next
            current.next = prev
            prev = current
            current = front

        return prev