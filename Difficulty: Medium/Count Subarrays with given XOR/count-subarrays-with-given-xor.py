class Solution:
    def subarrayXor(self, arr, k):
        prefix_xor=0
        count=0
        hash_map={0:1}
        
        for i in arr:
            prefix_xor ^= i
            x=prefix_xor^k
            if x in hash_map:
                count+=hash_map[x]
            
            if prefix_xor in hash_map:
                hash_map[prefix_xor]+=1
            else:
                hash_map[prefix_xor]=1
        return count