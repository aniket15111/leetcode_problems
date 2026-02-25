class Solution:
    def productExceptSelf(self, arr):
        total_product = 1
        zero_count = 0
        
        # First pass
        for num in arr:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num
        
        result = []
        
        # Second pass
        for num in arr:
            if zero_count > 1:
                result.append(0)
            elif zero_count == 1:
                if num == 0:
                    result.append(total_product)
                else:
                    result.append(0)
            else:
                result.append(total_product // num)
        
        return result