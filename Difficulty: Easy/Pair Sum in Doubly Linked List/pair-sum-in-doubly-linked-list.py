from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        ans=[]
        if not head:
            return ans
        left=head
        right=head
        
        while right.next:
            right=right.next
            
        while left!=right and right.next!=left:
            current_sum=left.data+right.data
            
            if current_sum==target:
                ans.append([left.data,right.data])
                left=left.next
                right=right.prev
                
            elif current_sum>target:
                right=right.prev
                
            else :
                left=left.next
            
                
        return ans
        
