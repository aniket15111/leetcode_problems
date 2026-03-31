class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        return self.binary_search(nums,i,j,target)

    def binary_search(self,nums,i,j,target):
        if i>j:
            return -1
        mid=(i+j)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            return self.binary_search(nums,mid+1,j,target)
        else:
            return self.binary_search(nums,i,mid-1,target)
            