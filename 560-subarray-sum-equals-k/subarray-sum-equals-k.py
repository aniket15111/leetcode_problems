class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        count=0
        hash_map={0:1}
        for i in nums:
            prefix_sum+=i
            if (prefix_sum-k) in hash_map:
                count+=hash_map[(prefix_sum-k)]
            if prefix_sum not in hash_map:
                hash_map[prefix_sum]=1
            else:
                hash_map[prefix_sum]+=1
        return count