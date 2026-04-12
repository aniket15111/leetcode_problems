class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count1=0
        count2=0
        for i in range(len(s)-1,-1,-1):
            if count1==0:
                if s[i]==' ':
                    continue
                else: 
                    count2+=1
                    count1+=1
            else:
                if s[i]==' ':
                    return count2
                count2+=1
                
        return count2
