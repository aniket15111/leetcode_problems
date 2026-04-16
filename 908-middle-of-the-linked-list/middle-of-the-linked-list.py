# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid=head
        current=head
        count=0

        while  mid and  mid.next :
            current=current.next
            mid=mid.next.next
        return current
        