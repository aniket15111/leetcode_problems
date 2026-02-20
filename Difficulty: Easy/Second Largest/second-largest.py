class Solution:
    def getSecondLargest(self, arr):
        largest = float('-inf')
        second_largest = float('-inf')
        for i in range(0,len(arr)):
            if(arr[i]>largest):
                second_largest=largest
                largest=arr[i]
            elif(arr[i]<largest  and arr[i]>second_largest and arr[i] != largest):
                second_largest=arr[i]
        if second_largest == float('-inf'):
            return -1

        return second_largest