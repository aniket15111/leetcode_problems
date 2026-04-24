# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        old_tail = head
        totalnode = 1
        while old_tail.next:
            old_tail = old_tail.next
            totalnode += 1
        
        old_tail.next = head

        k = k % totalnode
        steps_to_new_tail = totalnode - k
        
        while steps_to_new_tail > 0:
            old_tail = old_tail.next
            steps_to_new_tail -= 1
        
        new_head = old_tail.next
        old_tail.next = None

        return new_head

        return new_head

        
