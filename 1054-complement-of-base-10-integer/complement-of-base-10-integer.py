class Solution:
    def bitwiseComplement(self, n: int) -> int:
        ans=''
        to_bin=bin(n)[2:]
        
        xor='1'*len(to_bin)

        ans=int(to_bin,2)^int(xor,2)

        return ans