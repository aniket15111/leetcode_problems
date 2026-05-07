class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for i in num:
            while k>0 and st and st[-1]>i:
                st.pop()
                k-=1
            st.append(i)

        if k > 0:
            st = st[:-k]
        ans = ""
        for char in st:
            if not ans and char == '0':
                continue
            ans += char
            
        return ans if ans else "0"

