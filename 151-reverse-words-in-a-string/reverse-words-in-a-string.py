class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        size = len(s)
        ans = ''
        starting = 0
        
        for i in range(size):
            if s[i] == ' ':
                word = s[starting:i]
                if word:
                    ans = word + " " + ans
                starting = i + 1
        
        last_word = s[starting:]
        if last_word:
            ans = last_word + " " + ans
            
        return ans.strip()