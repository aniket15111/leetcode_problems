class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s=set(word)
        ans=0
        for i in range(26):
            lower=chr(ord('a')+i)
            upper=chr(ord('A')+i)

            if lower in s and upper in s:
                ans+=1
        return ans

