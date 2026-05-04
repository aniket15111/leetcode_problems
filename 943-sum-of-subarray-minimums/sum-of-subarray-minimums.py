class Solution:

    def nslfun(self,arr)->list:
        st=[]
        ans=[]
        for i in range(len(arr)):
            while st and arr[st[-1]]>arr[i]:
                st.pop()
            if not st:
                ans.append(-1)
            else:
                ans.append(st[-1])

            st.append(i)
        return ans

    def nsrfun(self,arr)->list:
        st=[]
        ans=[0]*len(arr)

        for i in range(len(arr)-1,-1,-1):
            while st and arr[st[-1]]>=arr[i]:
                st.pop()
            
            if not st:
                ans[i]=len(arr)
            else:
                ans[i]=st[-1]

            st.append(i)
        return ans
                

    def sumSubarrayMins(self, arr: List[int]) -> int:
        nsl=self.nslfun(arr)
        nsr=self.nsrfun(arr)
        total=0
        MOD = 10**9 + 7
        for i in range(len(arr)):
            count = (i - nsl[i]) * (nsr[i] - i)
            total = (total + (count * arr[i])) % MOD
        return total