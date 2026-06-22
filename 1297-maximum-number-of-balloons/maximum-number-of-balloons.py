class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        st={'b':0,'a':0,'l':0,'o':0,'n':0}


        for i in text:
            if i in st:
                st[i]+=1

        return min(st['b'],st['a'],st['l']//2,st['o']//2,st['n'])

        
