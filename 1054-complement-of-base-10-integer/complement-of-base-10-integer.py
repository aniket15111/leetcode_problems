class Solution:
    def bitwiseComplement(self, n: int) -> int:
        ans=''
        to_bin=bin(n)[2:]
        for i in to_bin:
            if i=='0':
                ans+='1'
            else:
                ans+='0'
        return int(ans,2)