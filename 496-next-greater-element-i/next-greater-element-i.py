class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        upd=0
        for i in nums1:
            for index,j in enumerate(nums2):
                nextmax=-1
                if j==i:
                    for k in range(index+1, len(nums2)):
                        if nums2[k]>i:
                            nextmax=nums2[k]
                            break
                    ans.append(nextmax)
                    break

        return ans
