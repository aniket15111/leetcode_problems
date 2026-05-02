class MinStack:

    def __init__(self):
        
        self.st=[]
        self.minval=None
    def push(self, val: int) -> None:
        if len(self.st)==0:
            self.st.append(0)
            self.minval=val

        else:
            self.st.append(val-self.minval)
            if val< self.minval:
                self.minval=val

    def pop(self) -> None:
        if not self.st:
            return 
        diff=self.st.pop()

        if diff<0:
            self.minval=self.minval-diff

    def top(self) -> int:
        diff=self.st[-1]
        if diff>0:
            return diff+self.minval
        else: 
            return self.minval


    def getMin(self) -> int:
        return self.minval


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()