class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour==12:
            hour=0
        ans=abs((30*hour)-(5.5*minutes))
        if ans >180:
            return 360-ans

        return ans