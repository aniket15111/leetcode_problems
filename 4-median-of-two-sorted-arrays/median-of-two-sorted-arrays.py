class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        total_len = n1 + n2
        mid_idx = total_len // 2
        
        i = j = count = 0
        curr = prev = 0

        while count <= mid_idx:
            prev = curr
            if i < n1 and (j >= n2 or nums1[i] < nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
            count += 1

        if total_len % 2 == 0:
            return (prev + curr) / 2.0
        else:
            return float(curr)