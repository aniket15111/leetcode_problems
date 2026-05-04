class Solution:

    def nglfun(self,arr):
        st=[]
        ans=[-1]*len(arr)

        for i in range(len(arr)):
            while st and arr[st[-1]]<arr[i]:
                st.pop()
            if not st:
                ans[i]=-1
            else:
                ans[i] = st[-1]
            st.append(i)
        return ans
    def ngrfun(self,arr):
        st=[]
        ans=[0]*len(arr)

        for i in range(len(arr)-1,-1,-1):
            while st and arr[st[-1]]<= arr[i]:
                st.pop()

            if not st:
                ans[i]=len(arr)
            else:
                ans[i]=st[-1]
            
            st.append(i)
        return ans
    def nslfun(self,arr):
        ans=[0]*len(arr)
        st=[]
        for i in range(len(arr)):
            while st and arr[st[-1]]>arr[i]:
                st.pop()

            if not st:
                ans[i]=-1
            else:
                ans[i]=st[-1]
            st.append(i)
        return ans

    def nsrfun(self,arr):
        ans=[0]*len(arr)
        st=[]
        for  i in range(len(arr)-1,-1,-1):
            while st and arr[st[-1]]>=arr[i]:
                st.pop()

            if not st:
                ans[i]=len(arr)
            else:
                ans[i]=st[-1]
            
            st.append(i)
        return ans
    def subArrayRanges(self, arr: List[int]) -> int:
        nsl=self.nslfun(arr)
        nsr=self.nsrfun(arr)
        ngl=self.nglfun(arr)
        ngr=self.ngrfun(arr)
        total=0
        for i in range(len(arr)):
            max_contribution = (i - ngl[i]) * (ngr[i] - i)
            min_contribution= (i-nsl[i]) * (nsr[i]-i)
            total += (max_contribution - min_contribution) * arr[i]
        return total