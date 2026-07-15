class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        lowest = 0
        low_digit = len(str(abs(low)))
        lowest_cnt = 1
        lowest_add = 0
        
        for i in range(low_digit):
            lowest = (lowest * 10) + lowest_cnt
            lowest_cnt += 1
            lowest_add = (lowest_add * 10) + 1
            
        lowest_ans = lowest
        ans = []
        
        while lowest_ans <= high:
            if lowest_ans >= low:
                ans.append(lowest_ans)
                
            lowest_ans += lowest_add

            if lowest_ans % 10 == 0 :
                if len(str(lowest_add)) == 9:
                    break
                    
                lowest_add = (lowest_add * 10) + 1
                lowest = (lowest * 10) + lowest_cnt
                lowest_cnt += 1
                lowest_ans = lowest
                
        return ans