# Problem: Min Stack
# Language: python3
# Runtime: 60 ms
# Memory: 18.3 MB

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._min = inf
        self.stack = []
    
    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append((val, min(self.stack[-1][1], val)))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()