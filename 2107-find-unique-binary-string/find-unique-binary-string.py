class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l = len(nums[0])
        
        for i in range(2**l):
            to_bit = bin(i)[2:]
            to_bit = '0'*(l - len(to_bit)) + to_bit
            
            if to_bit not in nums:
                return to_bit
            
