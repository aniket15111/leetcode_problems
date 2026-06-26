class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        prefix_cnt={0:1}

        current_sum=0
        ans=0
        smaller_cnt=0

        for num in nums:
            if num==target:
                smaller_cnt+=prefix_cnt.get(current_sum,0)
                current_sum+=1
            else:
                current_sum-=1
                smaller_cnt-=prefix_cnt.get(current_sum,0)

            ans+=smaller_cnt
            prefix_cnt[current_sum]=prefix_cnt.get(current_sum,0)+1
        return ans