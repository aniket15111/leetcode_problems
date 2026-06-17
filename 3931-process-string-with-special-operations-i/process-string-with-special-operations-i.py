class Solution:
    def processStr(self, s: str) -> str:
        result=[]
        for i in s:
            if i=='#':
                for j in range(len(result)):
                    result.append(result[j])
            elif i=='*':
                if result:
                    result.pop()
                
            elif i=='%':
                result.reverse()
            else:
                result.append(i)
        return ''.join(result)
