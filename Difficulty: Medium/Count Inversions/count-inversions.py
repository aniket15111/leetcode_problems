class Solution:
    def merge(self, a, low, mid, high):
        temp = []
        i = low
        j = mid + 1
        count = 0  
        
        while (i <= mid and j <= high):
            if a[i] <= a[j]:
                temp.append(a[i])
                i += 1
            else:

                count += (mid - i + 1) 
                temp.append(a[j])
                j += 1
                
        while i <= mid:
            temp.append(a[i])
            i += 1
        while j <= high:
            temp.append(a[j])
            j += 1
            
        for k in range(len(temp)):
            a[low + k] = temp[k]
            
        return count

    def merge_sort(self, a, low, high):
        count = 0
        if low < high:
            mid = (low + high) // 2
            count += self.merge_sort(a, low, mid)
            count += self.merge_sort(a, mid + 1, high)
            count += self.merge(a, low, mid, high)
        return count

    def inversionCount(self, arr):
        return self.merge_sort(arr, 0, len(arr) - 1)