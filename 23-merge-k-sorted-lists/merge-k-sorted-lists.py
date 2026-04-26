# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans=[]

        for i in lists:
            temp=i
            while temp:
                ans.append(temp.val)
                temp=temp.next
        ans.sort()

        dummy=ListNode(-1)
        temp=dummy

        for i in ans:
            temp.next=ListNode(i)
            temp=temp.next
        return dummy.next