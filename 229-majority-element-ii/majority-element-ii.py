from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        result = []

        count = 1

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                if count > n // 3:
                    result.append(nums[i - 1])
                count = 1 

        if count > n // 3:
            result.append(nums[-1])

        return result