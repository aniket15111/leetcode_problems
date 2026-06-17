class Solution:
    def processStr(self, s: str) -> str:
        result=deque()
        is_reversed=False
        for i in s:
            if i=='#':
                curr=list(result)
                if is_reversed:
                    result.extendleft(reversed(curr))
                else:
                    result.extend(curr)
            elif i=='*':
                if result:
                    if is_reversed:
                        result.popleft()
                    else:
                        result.pop()
                
            elif i=='%':
                is_reversed=not is_reversed
            else:
                if is_reversed:
                    result.appendleft(i)
                else:
                    result.append(i)

        final=list(result)
        if is_reversed:
            final.reverse()
        return ''.join(final)
