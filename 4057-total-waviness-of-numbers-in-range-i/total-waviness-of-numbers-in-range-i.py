class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def peak_check(num):
            cnt=0
            for i in range(1,len(num)-1):
                centre=int(num[i])
                left=int(num[i-1])  
                right=int(num[i+1])
                if centre>left and centre >right:
                    cnt+=1
                elif centre<left and centre<right:
                    cnt+=1
            return cnt

        if num1 < 100:
            if num2 <= 100:
                return 0
            else:
                num1 = 100

        ans = 0
        for i in range(num1, num2 + 1):
            ans += peak_check(str(i))
        return ans