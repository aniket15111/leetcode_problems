class Solution:
    def missingNum(self, arr):
        length=len(arr)+1
        arr_sum=sum(arr)
        expected_sum=length*(1+length)*0.5
        missing=expected_sum-arr_sum
        return int(missing)