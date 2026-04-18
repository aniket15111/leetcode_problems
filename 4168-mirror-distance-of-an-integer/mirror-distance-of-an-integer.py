class Solution:
    def mirrorDistance(self, n: int) -> int:
        new=0
        temp=n
        while temp>0:
            digit=temp%10
            new=new*10+digit
            temp=temp//10
        return abs(new-n)