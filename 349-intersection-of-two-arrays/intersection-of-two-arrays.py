class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=set()
        for i in nums1:
            for j in range(len(nums2)):
                if i==nums2[j]:
                    ans.add(i)
                    nums2[j]=-1
                    break
        return list(ans)