class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans=float('inf')
        fin1=float('inf')
        ind=-1

        for i in range(len(landStartTime)):
            total=landStartTime[i]+landDuration[i]
            if total<fin1:
                fin1=total
                ind=i


        for i in range(len(waterStartTime)):
            fin2=max(fin1,waterStartTime[i])+waterDuration[i]
            ans=min(ans,fin2)

        fin1=float('inf')
        for i in range(len(waterStartTime)):
            total=waterStartTime[i]+waterDuration[i]
            if total<fin1:
                fin1=total
                ind=i


        for i in range(len(landStartTime)):
            fin2=max(fin1,landStartTime[i])+landDuration[i]
            ans=min(ans,fin2)



        return ans