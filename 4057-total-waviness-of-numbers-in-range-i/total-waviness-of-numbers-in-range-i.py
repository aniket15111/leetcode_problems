class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def peak_check(num):
            prev = None
            cnt = 0
            while num > 0:
                # Stop only when we don't even have a 'left' digit left to check
                if num // 10 == 0:
                    break
                
                if prev is None:
                    prev = num % 10
                
                center = num % 10
                left = (num // 10) % 10      
                
                if center > prev and center > left:
                    cnt += 1
                elif center < prev and center < left:
                    cnt += 1
                    
                prev = center
                num = num // 10
                    
            return cnt

        if num1 < 100:
            if num2 <= 100:
                return 0
            else:
                num1 = 100

        ans = 0
        for i in range(num1, num2 + 1):
            ans += peak_check(i)
        return ans