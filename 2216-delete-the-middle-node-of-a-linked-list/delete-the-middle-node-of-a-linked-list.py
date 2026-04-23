# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        first=False

        while fast and fast.next:
            fast=fast.next.next
            if first==False:
                first=True
                continue
            slow=slow.next
        if slow==fast:
            return None
        slow.next=slow.next.next

        return head