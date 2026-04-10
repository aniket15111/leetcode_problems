class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        n1, n2 = len(num1), len(num2)

        if n1 > n2:
            return self.findMedianSortedArrays(num2, num1)

        i, j = 0, n1
        left_size = (n1 + n2 + 1) // 2

        while i <= j:
            mid1 = (i + j) // 2
            mid2 = left_size - mid1

            l1 = num1[mid1 - 1] if mid1 > 0 else float('-inf')
            r1 = num1[mid1] if mid1 < n1 else float('inf')
            
            l2 = num2[mid2 - 1] if mid2 > 0 else float('-inf')
            r2 = num2[mid2] if mid2 < n2 else float('inf')

            if l1 <= r2 and l2 <= r1:
                if (n1 + n2) % 2 == 1:
                    return float(max(l1, l2))
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0

            elif l1 > r2:
                j = mid1 - 1
            else:
                i = mid1 + 1

        return 0.0