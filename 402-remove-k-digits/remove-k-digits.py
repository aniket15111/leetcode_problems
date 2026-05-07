class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for i in num:
            while k>0 and st and st[-1]>i:
                st.pop()
                k-=1
            st.append(i)

        final_stack=st[:-k] if k>0 else st
        ans=''.join(final_stack).lstrip('0')

        return ans if ans else '0'

