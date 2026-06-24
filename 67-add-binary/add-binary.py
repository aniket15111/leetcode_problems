class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans=[0]*max(len(a),len(b))
        n=len(ans)-1
        m=len(a)-1
        o=len(b)-1
        nxt=0
        for i in range(max(m+1,o+1)):
            bit_a = a[m] if m >= 0 else '0'
            bit_b = b[o] if o >= 0 else '0'
            if bit_a=='0' and bit_b=='0':
                if nxt==1:
                    sumi=1
                    nxt=0
                else:
                    sumi=0
                    nxt=0
            elif bit_a=='1' and bit_b=='1':
                if nxt==1:
                    sumi=1
                    nxt=1
                else:
                    sumi=0
                    nxt=1
            else:
                if nxt==1:
                    sumi=0
                    nxt=1
                else:
                    sumi=1
                    nxt=0
            ans[n]=sumi
            m-=1
            n-=1
            o-=1
        if nxt == 1:
            return '1'+"".join(map(str, ans))
        else:
            return "".join(map(str, ans))

