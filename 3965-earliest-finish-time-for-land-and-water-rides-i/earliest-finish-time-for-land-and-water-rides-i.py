class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans=float('inf')


        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                current_time=0
                current_time+=landStartTime[i]+landDuration[i]
                current_time=max(current_time,waterStartTime[j])
                current_time+=waterDuration[j]
                ans=min(ans,current_time)


        for i in range(len(waterStartTime)):
            current_time=0
            for j in range(len(landStartTime)):
                current_time=0
                current_time+=waterStartTime[i]+waterDuration[i]
                current_time=max(current_time,landStartTime[j])
                current_time+=landDuration[j]
                ans=min(ans,current_time)

        return ans


