class Solution:
    def kthElement(self, a, b, k):
        n1 = len(a)
        n2 = len(b)
        
        if n1 > n2:
            return self.kthElement(b, a, k)

        i = max(0, k - n2)
        j = min(k, n1)
        
        while i <= j:
            mid1 = (i + j) // 2
            mid2 = k - mid1
            
            l1 = a[mid1 - 1] if mid1 > 0 else float('-inf')
            r1 = a[mid1] if mid1 < n1 else float('inf')
            
            l2 = b[mid2 - 1] if mid2 > 0 else float('-inf')
            r2 = b[mid2] if mid2 < n2 else float('inf')
            
            if l1 <= r2 and l2 <= r1:
                return int(max(l1, l2))
            elif l1 > r2:
                j = mid1 - 1
            else:
                i = mid1 + 1
                
        return 0