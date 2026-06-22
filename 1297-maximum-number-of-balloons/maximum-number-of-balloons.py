class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        st={'b':0,'a':0,'l':0,'o':0,'n':0}


        for i in text:
            if i in st:
                st[i]+=1
        ans=-1
        bal_str='balloon'
        not_avl=True
        while True:
            for i in bal_str:
                if st[i]!=0:
                    st[i]-=1
                else:
                    not_avl=False
                    break
            ans+=1
            
            if not not_avl:
                break

        return ans


        
