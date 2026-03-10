class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table={}
        for i in nums:
            if i not in hash_table:
                hash_table[i]=1
            else:
                hash_table[i]+=1
            
        sorted_items = sorted(hash_table.items(), key=lambda x: x[1], reverse=True)
       
        return  [key for key, value in sorted_items[:k]]