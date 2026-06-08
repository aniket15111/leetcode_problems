class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivot_element=[]
        left=[]
        right=[]

        for i in nums:
            if i <pivot:
                left.append(i)
            elif i>pivot:
                right.append(i)
            else:
                pivot_element.append(i)        



        return left+pivot_element+right