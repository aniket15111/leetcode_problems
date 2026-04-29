class MyStack:

    def __init__(self):
         self.q=deque()

    def push(self, x: int) -> None:
        s=len(self.q)
        self.q.append(x)
        for i in range(s):
            self.q.append(self.q[0])
            self.q.popleft()



    def pop(self) -> int:
        if self.q:
           return self.q.popleft()

    def top(self) -> int:
        if self.q:
            return self.q[0]
        else:
            return -1

    def empty(self) -> bool:
        if self.q:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()