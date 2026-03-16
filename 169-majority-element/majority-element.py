class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums1 = {}

        for i in nums:
            if i not in nums1:
                nums1[i] = 1
            else:
                nums1[i] += 1

        return max(nums1, key=nums1.get)