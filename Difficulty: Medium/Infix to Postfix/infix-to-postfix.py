def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

class Solution:
    def infixtoPostfix(self, s):
        ans = []
        st = []
        
        for i in s:
            if i.isalnum():
                ans.append(i)
            
            elif i == '(':
                st.append(i)
                
            elif i == ')':
                while st and st[-1] != '(':
                    ans.append(st.pop())
                st.pop() 
            
            else:
                while st and st[-1] != '(':
                    if i == '^':
                        if prec(st[-1]) > prec(i):
                            ans.append(st.pop())
                        else:
                            break
                    else:
                        if prec(st[-1]) >= prec(i):
                            ans.append(st.pop())
                        else:
                            break
                st.append(i)
        
        while st:
            ans.append(st.pop())
            
        return ''.join(ans)