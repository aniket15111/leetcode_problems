# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:

    def middle(self,head):
        fast=head.next
        slow=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

    def merge(self,left,right):
        dummy=ListNode(-1)
        temp=dummy
        while left and right:
            if left.val<right.val:
                temp.next=left
                left=left.next
            else:
                temp.next=right
                right=right.next
            temp=temp.next

        temp.next=left if left else right
        return dummy.next
            

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        mid=self.middle(head)
        left=head
        right=mid.next
        mid.next=None
        left=self.sortList(left)
        right=self.sortList(right)
        head=self.merge(left,right)
        return head 

        