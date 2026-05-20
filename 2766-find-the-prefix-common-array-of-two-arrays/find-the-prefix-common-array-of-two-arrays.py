class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set1=set()
        set2=set()
        cmncnt=0
        ans=[]
        for i in range(len(A)):

            if A[i]==B[i] :
                cmncnt+=1
            else:
                if A[i] in set2:
                    cmncnt+=1
                if B[i] in set1:
                    cmncnt+=1

            set1.add(A[i])
            set2.add(B[i])
            ans.append(cmncnt)

        return ans
            