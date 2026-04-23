# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def search(self, temp,k):
        while temp and k>1:
            temp=temp.next
            k-=1
        return temp

    def reversel(self, temp):
        prev = None
        curr = temp
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k==1:
            return head
        dummy= ListNode(0)
        dummy.next=head
        before_group=dummy
        temp=head

        while temp:
            #search for the kth node
            kthnode=self.search(temp,k)
            if not kthnode:
                break


            oldnext=kthnode.next
            kthnode.next=None
            

            #reversing
            new_group_head=self.reversel(temp)

            before_group.next=new_group_head

            temp.next=oldnext

            before_group=temp
            temp=oldnext
        
        return dummy.next