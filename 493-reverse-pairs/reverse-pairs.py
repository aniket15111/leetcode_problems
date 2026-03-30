class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return self.merge_count(nums,0,len(nums)-1)

    def merge_count(self,arr,low,high):
        count=0
        if low<high:
            mid=(low+high)//2
            count+=self.merge_count(arr,low,mid)
            count+=self.merge_count(arr,mid+1,high)
            count+=self.count(arr,low,mid,high)
            self.merge(arr,low,mid,high)
        return count

    def count(self,arr,low,mid,high):
        j=mid+1
        i=low
        count=0
        while i <= mid:
            while j <= high and arr[i] > 2 * arr[j]:
                j += 1
            count += (j - (mid + 1))
            i += 1
            
        return count



    def merge(self, a, low, mid, high):
        temp = []
        i = low
        j = mid + 1
        
        while (i <= mid and j <= high):
            if a[i] <= a[j]:
                temp.append(a[i])
                i += 1
            else:
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
        